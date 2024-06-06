import ollama

def generate_weather_response(query , context):
    template  = f"""
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
"""
    
    formatted_prompt = f"{template}\n\nContext: {context}"
    llm_response = ollama.chat(model='gemma:2b', messages=[{'role': 'user', 'content': formatted_prompt}])
    return llm_response['message']['content']

if __name__ == "__main__":
    query="Give me an idea about weather on 22nd March"

    context = """
{
    date : "22.03.2023" ,
    temperature : "44 degree - 46 dgree celsisus" ,
    weather : "sunny" ,
}
"""
    print(generate_weather_response(query , context))

    query = "Hey, what's the weather like in San Francisco right now? I'm planning a trip there next week and want to know what to expect"

    context = """
{
  "location": "San Francisco",
  "date": "2024-05-10",
  "weather": {
    "temperature": "62°F",
    "condition": "Partly Cloudy",
    "humidity": "72%",
    "wind": "7 mph NW"
  }
}

"""
    print(generate_weather_response(query , context))
