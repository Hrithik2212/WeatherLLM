import ollama 
import weather_functions


PROMPT = \
'''
Given the user query , identify the city the user is asking about
If there is country name but not city name then respond the country's capital city name 
Respond with nothing but the city name only if it exists else respond null, such that I can directly execute your function call without any post processing necessary from my end. Do not use variables.
NOTE : Do not respond with country name and output only the city name in one word or two words
User Query: {query}
'''

# llm_response = ollama.chat(model='gemma:2b', messages=[{'role': 'Function chooser', 'content': PROMPT}])


if __name__ == "__main__":
    query = "What is the weather in new york"
    prompt = PROMPT.format(query = query)
    # print(prompt)
    llm_response = ollama.chat(model='gemma:2b', messages=[{'role': 'system', 'content': prompt}])
    print(llm_response['message']['content'])

