import requests 
import json 
from pprint import pprint as pp
import pandas as pd 
from datetime import datetime



def get_weather_data(coordinates , start_date = str(datetime.now())[:10] , end_date = str(datetime.now())[:10] ):
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Args:
    coordinates (tuple): The latitude of the location.

    Returns:
    float: The current temperature in the coordinates you've asked for
    """
    latitude, longitude = coordinates
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": latitude,
	"longitude": longitude,
	"current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "rain", "showers", "snowfall"],
	"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "rain", "showers", "snowfall", "cloud_cover"],
	"timezone": "GMT",
	"start_date": start_date,
	"end_date": end_date
}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        #print (f"""Temperature in C: {response.json()["current"]["temperature_2m"]}""")
        return response.json()
    else:
        return {"error": "Failed to fetch data, status code: {}".format(response.status_code)}


def get_coordinates_from_city(city_name):
    """
    Fetches the latitude and longitude of a given city name using the Maps.co Geocoding API.

    Args:
    city_name (str): The name of the city.

    Returns:
    tuple: The latitude and longitude of the city.
    """
    base_url = "https://geocode.maps.co/search"
    params = {"q": city_name}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Assuming the first result is the most relevant
            return data[0]["lat"], data[0]["lon"]
        else:
            return {"error": "No data found for the given city name."}
    else:
        return {"error": "Failed to fetch data, status code: {}".format(response.status_code)}


def aggreagate_weather_data_by_days(weather_data:dict):
    weather_units = weather_data['hourly_units']
    weather_data = pd.DataFrame(weather_data['hourly'])
    weather_data['time'] = pd.to_datetime(weather_data['time'])
    weather_data['date'] = weather_data['time'].dt.date
    daily_mean_df =  weather_data.groupby('date').mean().reset_index()
    daily_mean_df.set_index('date' , inplace=True)
    return {'weather data' : daily_mean_df.to_dict() , 'weather_units' : weather_units} 

if __name__ == "__main__" :
    # Testing 
    city = "chennai" # input("Enter the city name : ")
    response  =  get_coordinates_from_city(city.lower())
    try :
        lat , lon = response 
        print(f"The geo-position of {city.split()[0]} is "+str({"lat":lat , "long":lon}))
    except :
        print(response)

    weather = get_weather_data((lat , lon))
    data = pd.DataFrame(weather['hourly'])


    print(data)
