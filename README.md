**Code Documentation for Humorous Weather Chat-bot**
=====================================================

By Hrithik Reddy
June 14th, 2024

OS Requirements
-------------------

The following code is only tested on Ubuntu 23.10 (Mantic Minotaur). 
However, the Python dependencies will also work for Mac OS, Windows 11, 
and other distributions of Linux.

Packages Required
---------------------

The project was developed on the following versions:

* Python - 3.11.6
* NPM - 9.2.0
* Node - v18.13.9

Setup Instructions to run the web application
-------------------------------------------------

1. Open the terminal and clone the repository from GitHub along with the 
private access token:
```
git clone https://github.com/Hrithik2212/WeatherLLM.git
```
2. Navigate to the backend directory:
```
cd backend
```
3. Setup the python virtual environment 
```
python3 -m venv venv
```
4. Intall requirements file with pip command 
```
pip3 install -r requirements.txt 
```
5. Sign up to Groq Cloud and get the GROQ API key , paste the GROQ API key to .env file as shown and save the file
```
GROQ_API_KEY=”YOUR_API_KEY”
```
6. Start the FastAPI backend server:
```
uvicorn main:app --reload
```
7. Open a new terminal in the root directory of the application and navigate to the frontend dir and install the packages 
```
cd frontend
npm install
```


8. Start the react server :
```
npm start
```

## API Documentation
------------------------

### 1. POST /weather

This endpoint processes a user query related to weather information or general chit-chat. It extracts entities from the query, determines the appropriate humorous response, and fetches weather data if needed.
#### Request Body
query (str): The user's query.

default_city (Optional[str]): The default city to use if no city is specified in the query.

widget_city (Optional[str]): The city from the weather widget

#### Example Request
```
{
  "query": "What is the weather in New York tomorrow?",
  "default_city": "New York",
  "widget_city": "New York"
}
```
#### Response

response (str): The response to the user's query.
error (str): Error message if there is an issue.

#### Example Response
```
{
  "response": "🌞️ Ah, New York tomorrow? Well, it's going to be a scorcher! Temperatures will soar to a sizzling 21°C (that's 70°F for you Fahrenheit fans). And don't even get me started on the humidity - it's going to be a sticky 69%! But hey, at least the sun will be shining brightly, with a cloud cover of 31%! 🌞️"
}
```
#### Description
* Extracts entities from the user query using an entity extractor.
* Determines if the query is a chit-chat or weather-related query.
* If chit-chat, responds using a chit-chat agent.
* If weather-related, determines the city and date range for the weather query.
* Fetches weather data based on the extracted entities and the provided city.
* Uses a humour agent to generate a response with the weather data context.


### 2. POST /weather_forecast

This endpoint retrieves weather data for a specific city and aggregates the data by day forecasted upto 5 days.
#### Request Body
widget_city (str): The city for which weather data is to be retrieved.

#### Example Request
```
{
  "widget_city": "New york"
}
```

#### Response
weather_data (dict): Aggregated weather data by day.
weather_units (dict): Units of the weather data.
error (str): Error message if there is an issue.

#### Example Response
```
{
  "weather data": {
    "temperature_2m": {
      "2024-06-14": 31.616666666666664,
      "2024-06-15": 32.079166666666666,
      "2024-06-16": 32.42916666666667,
      "2024-06-17": 32.583333333333336,
      "2024-06-18": 32.74583333333333,
      "2024-06-19": 32.824999999999996
    },
    "relative_humidity_2m": {
      "2024-06-14": 64.29166666666667,
      "2024-06-15": 61.041666666666664,
      "2024-06-16": 60.375,
      "2024-06-17": 62.666666666666664,
      "2024-06-18": 63.583333333333336,
      "2024-06-19": 61.125
    },
    "dew_point_2m": {
      "2024-06-14": 23.712500000000002,
      "2024-06-15": 23.204166666666666,
      "2024-06-16": 23.28333333333333,
      "2024-06-17": 23.84583333333333,
      "2024-06-18": 24.104166666666668,
      "2024-06-19": 23.6375
    },
    "rain": {
      "2024-06-14": 0,
      "2024-06-15": 0,
      "2024-06-16": 0,
      "2024-06-17": 0,
      "2024-06-18": 0,
      "2024-06-19": 0
    },
    "showers": {
      "2024-06-14": 0,
      "2024-06-15": 0,
      "2024-06-16": 0,
      "2024-06-17": 0,
      "2024-06-18": 0.0375,
      "2024-06-19": 0.012500000000000002
    },
    "snowfall": {
      "2024-06-14": 0,
      "2024-06-15": 0,
      "2024-06-16": 0,
      "2024-06-17": 0,
      "2024-06-18": 0,
      "2024-06-19": 0
    },
    "cloud_cover": {
      "2024-06-14": 99.875,
      "2024-06-15": 99.95833333333333,
      "2024-06-16": 100,
      "2024-06-17": 100,
      "2024-06-18": 74.125,
      "2024-06-19": 88
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
```
#### Description
* Retrieves geographical coordinates for the specified city.
* Fetches weather data for the city for the next five days.
* Aggregates(mean) the weather data by day.
* Returns the aggregated weather data along with the units.



### 3. GET /health

This endpoint checks the health status of the backend application.
#### Response
message (str): A message indicating the health status of the backend application.
#### Example Response
```
{
  "message": "The backend application is healthy"
}
```
#### Description
* This endpoint is used to verify that the backend application is running and healthy.
