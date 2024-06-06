
from typing import Dict, List, Optional, Type

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field , Extra , ValidationError
from langchain.tools import BaseTool
from langchain_community.chat_models import ChatOllama
from pprint import pprint as pp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
 
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(temperature=0,groq_api_key= GROQ_API_KEY,  model_name="llama3-8b-8192")

def remove_lucene_chars(text: str) -> str:
    """Remove Lucene special characters"""
    special_chars = [
        "+",
        "-",
        "&",
        "|",
        "!",
        "(",
        ")",
        "{",
        "}",
        "[",
        "]",
        "^",
        '"',
        "~",
        "*",
        "?",
        ":",
        "\\",
    ]
    for char in special_chars:
        if char in text:
            text = text.replace(char, " ")
    return text.strip()



def generate_full_text_query(input: str, type: str) -> str:
    """
    Generate a full-text search query for a given input string.

    This function constructs a query string suitable for a full-text search.
    It processes the input string by splitting it into words and appending a
    similarity threshold (~0.8) to each word, then combines them using the AND
    operator. Useful for mapping movies and people from user questions
    to database values, and allows for some misspelings.
    """
    property_map = {"movie": "title", "person": "name"}
    full_text_query = ""
    words = [el for el in remove_lucene_chars(input).split() if el]
    for word in words[:-1]:
        full_text_query += f" {property_map[type]}:{word}~0.8 AND"
    full_text_query += f" {property_map[type]}:{words[-1]}~0.8"
    return full_text_query.strip()




class QueryAgentDataParser(BaseModel):
    chit_chat: Optional[bool] = Field(description="Boolean value wether the given query is chit chat or weather related query")
    city_entity: Optional[List[str]] = Field(description="list of city names in the given query")
    state_entity: Optional[List[str]] = Field(description="list of state names in the given query")
    country_entity : Optional[List[str]] = Field(description="list of country names in the given query")
    time_entity : Optional[List[str]] = Field(description='list of time str either dates or nouns like Today , Yesterday , Now ,Next Week , etc...')
    forecast : Optional[bool] = Field(description="boolean value statting wether the given query is for forecast or not")
    history : Optional[bool] = Field(description="Boolean value stating wether the given query  enquires about past weather data")

    class Config :
        extra = Extra.forbid

#### Testing #### 
# query = "Thinking about going solar to save some green and help the planet! Can you tell me how much sunshine to expect in chennai for the next week or so?"
# query = "How will be waether in chennai from June 3rd to June 10th"
# query = "Hi , I am Hrithik , What about you"
# query = "Can you tell me about last weeks weather in chennai"
query = "Hows the weather in Chennai"
# llm_model = ChatOllama(model='llama3')


parser = JsonOutputParser(pydantic_object=QueryAgentDataParser)


def JSON_Extract(query):
    # Extract tweet text
    print(query)

    # Define a prompt template for assessing tweet content
    # and include the formatting instructions 
    prompt = PromptTemplate(
        template="""
        Assess and identfiy cities , country , states if any present in the query. 
        Assess and identfiy time nouns or dates (eg 24th May , 5-7-2023 , Next Week , Coming Saturday)present in the query. 
        Assess if the tweet is related to weather or not 
        Assess if the tweet is about forecast or not 
        Assess if the tweet is about historical weather or not
        If there are any speeling mistakes especially in city name then correct them  
        {format_instructions}
        
        Query : {query}
        """,
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    # Construct a Langchain Chain to connect the prompt template with the LLM and Pydantic parser
    chain = prompt | llm_model | parser
    result = chain.invoke({"query": query})
    
    pp(result)
    print(type(result))
    print("------")\

print()
pp(parser.get_format_instructions())    
JSON_Extract(query=query)
