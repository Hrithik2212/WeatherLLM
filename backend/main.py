from langchain_groq import ChatGroq
from dotenv import load_dotenv 
import os 
from pprint import pprint as pp 
from agents import EntityExtractorAgent  , ChitChatAgent , TimeExtractorAgent , HumourousAgent 
from fastapi import FastAPI 
from api_models import UserQueryModel , WidgetData
from data_apis import * 
import pandas as pd 
from datetime import datetime , timedelta
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app =  FastAPI() 


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(temperature=0,groq_api_key= GROQ_API_KEY,  model_name="llama3-8b-8192")


extractor = EntityExtractorAgent(llm = llm_model)
chit_chat_agent = ChitChatAgent(llm = llm_model) 
time_extractor_agent = TimeExtractorAgent(llm = llm_model)
humour_agent = HumourousAgent(llm = llm_model)

# query = "Feeling a little stuffy lately.  Wondering if it's the weather or the air quality acting up in Chennai.  Anything funky in the forecast that might explain it?"

@app.get('/health') 
def check_backend() :
    return {'message' : "The backend application is healthy "}


@app.post('/post_query')
def weather_query(request:UserQueryModel) : 
    query = request.query 
    default_city = request.default_city
    widget_city = request.widget_city 
    # Extract entitties from the query 
    entities  = extractor.extract_entity(query)
    print(entities)

    if entities['chit_chat'] : 
        return {'response':chit_chat_agent.chat(query)}
    
    if entities['city_entity']: 
        city = entities['city_entity'][0].lower()
    else : 
        city = default_city.lower()

    date_range = time_extractor_agent.get_time_data(entities['time_entity'])
    
    date_range = {"start_date" : date_range['start_date'][:10] , "end_date" : date_range['end_date'][:10]} 
    if not entities['forecast'] : 
        date_range['start_date'] = str(datetime.now())[:10]  
    # print(date_range)
    if entities['history'] : 
        response = humour_agent.chat(query , context = "We don't have acces to any hsitorical data and thus won't be able to answer the user's query")
        return {'response' : response}
    geo_data = get_coordinates_from_city(city) 
    try : 
        lat , long = geo_data 
    except : 
        print(geo_data['error'])
        return {'error' : geo_data['error'] , "Type" : "Weatgher API error"}
    
    weather_data = get_weather_data((lat , long), date_range['start_date'], date_range['end_date'])
    # print(weather_data)
    weather_data = aggreagate_weather_data_by_days(weather_data=weather_data) 
    print(weather_data)
    # Implement spell check and city map 
    response = humour_agent.chat(query , context = weather_data)
    return {'response' : response}


@app.post('/get_weather_data')
def get_data_for_city(widget_data : WidgetData ): 
    city = widget_data.widget_city 
    try : 
        geo_data = get_coordinates_from_city(city.lower()) 
    except : 
        return {"error":geo_data['error'] , 'type':"GeoAPI Error"} 
    lat , long =  geo_data
    today_date = str(datetime.now())[:10] 
    end_date = str(datetime.now()  + timedelta(5))[:10] 
    print(end_date)

    weather_data = get_weather_data((lat , long) ,today_date ,end_date )
    weather_units = weather_data['hourly_units']
    weather_data = pd.DataFrame(weather_data['hourly'])

    weather_data['time'] = pd.to_datetime(weather_data['time'])

    # Extract the date part
    weather_data['date'] = weather_data['time'].dt.date

    # Group by the date and compute the mean
    daily_mean_df = weather_data.groupby('date').mean().reset_index()
    daily_mean_df.set_index('date' , inplace=True)
    print(daily_mean_df)
    daily_mean_df.drop(['time'] , axis=1 , inplace=True)
    return {'weather data' : daily_mean_df.to_dict() , 'weather_units' : weather_units} 


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)