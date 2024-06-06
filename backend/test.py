from langchain_groq import ChatGroq
from dotenv import load_dotenv 
import os 
from pprint import pprint as pp 
from testing.agents import EntityExtractorAgent , TimeExtractorAgent


load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(temperature=0,groq_api_key= GROQ_API_KEY,  model_name="llama3-8b-8192")

def test_entity_extraction():
    agent = EntityExtractorAgent(llm = llm_model)
    query = "Feeling a little stuffy lately.  Wondering if it's the weather or the air quality acting up in Chennai.  Anything funky in the forecast that might explain it?"
    pp(agent.extract_entity(query))

def test_time_extracrtion_agent() : 
    time_agent = TimeExtractorAgent(llm = llm_model)
    extract_agent = EntityExtractorAgent(llm = llm_model)
    query = "Feeling a little stuffy lately.  Wondering if it's the weather or the air quality acting up in Chennai.  Anything funky in the forecast that might explain it?"
    response = extract_agent.extract_entity(query)['time_entity']
    print(response)
    response = (", ").join(response)
    # pp(time_agent.prompt)
    pp(time_agent.get_time_data(response))


if __name__ == "__main__":
    # Test 1
    # test_entity_extraction()
    # Test 2
    test_time_extracrtion_agent()
