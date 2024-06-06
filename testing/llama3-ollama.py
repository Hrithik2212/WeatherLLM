from langchain_groq import ChatGroq
from dotenv import load_dotenv 
import os 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(temperature=0,groq_api_key= GROQ_API_KEY,  model_name="llama3-8b-8192")


def generate_weather_response(query , context):
    prompt = PromptTemplate(template  = """
You are an incredibly wise, smart, witty and humours knowlegable weather announcement assistant

% RESPONSE TONE:

- Your response should have humor, sarcasm and should tease the reader.

% RESPONSE FORMAT:

- Respond in under 200 characters
- Respond in two or less short sentences
- You can use emojis if it makes response more funny.
- Do not include the initial response phrases like "Here is the resonse" or "Here is the prediction" or any such phrase. Just directly give the response.

% RESPONSE CONTENT:

- Do not deviate from the users question 

Keep in mind all of the above things while generating a response for the query provided ahead: 

query : {query}

Context : {context}
""" , 
input_variables=['query', 'context']
    )
    parser = StrOutputParser() 
    chain = prompt | llm_model | parser
    return chain.invoke({'query' : query , 'context' :context})
    
if __name__ == "__main__":
    query="Can I play cricket on june 6th"

    context = """
{
  "weather data": {
    "temperature_2m": {
      "2024-06-06": 30.141666666666666,
      "2024-06-07": 30.412499999999998,
      "2024-06-08": 31.0625,
      "2024-06-09": 31.599999999999998,
      "2024-06-10": 32.208333333333336,
      "2024-06-11": 31.833333333333332
    },
    "relative_humidity_2m": {
      "2024-06-06": 76.58333333333333,
      "2024-06-07": 76.125,
      "2024-06-08": 69.33333333333333,
      "2024-06-09": 65.875,
      "2024-06-10": 63.083333333333336,
      "2024-06-11": 64.5
    },
    "dew_point_2m": {
      "2024-06-06": 25.383333333333336,
      "2024-06-07": 25.579166666666666,
      "2024-06-08": 24.45,
      "2024-06-09": 23.883333333333336,
      "2024-06-10": 23.429166666666664,
      "2024-06-11": 23.78333333333333
    },
    "rain": {
      "2024-06-06": 0,
      "2024-06-07": 0,
      "2024-06-08": 0,
      "2024-06-09": 0,
      "2024-06-10": 0,
      "2024-06-11": 0
    },
    "showers": {
      "2024-06-06": 0.325,
      "2024-06-07": 0.0625,
      "2024-06-08": 0.1125,
      "2024-06-09": 0,
      "2024-06-10": 0.012500000000000002,
      "2024-06-11": 0.025000000000000005
    },
    "snowfall": {
      "2024-06-06": 0,
      "2024-06-07": 0,
      "2024-06-08": 0,
      "2024-06-09": 0,
      "2024-06-10": 0,
      "2024-06-11": 0
    },
    "cloud_cover": {
      "2024-06-06": 98.70833333333333,
      "2024-06-07": 99.75,
      "2024-06-08": 99.58333333333333,
      "2024-06-09": 75.83333333333333,
      "2024-06-10": 82.75,
      "2024-06-11": 98.25
    }
  },
  "weather_units": {
    "time": "iso8601",
    "temperature_2m": "°C",
    "relative_humidity_2m": "%",
    "dew_point_2m": "°C",
    "rain": "mm",
    "showers": "mm",
    "snowfall": "cm",
    "cloud_cover": "%"
  }
}
"""
    print(generate_weather_response(query , context))

#     query = "Hey, what's the weather like in San Francisco right now? I'm planning a trip there next week and want to know what to expect"

#     context = """
# {
#   "location": "San Francisco",
#   "date": "2024-05-10",
#   "weather": {
#     "temperature": "62°F",
#     "condition": "Partly Cloudy",
#     "humidity": "72%",
#     "wind": "7 mph NW"
#   }
# }

# """
#     print(generate_weather_response(query , context))
