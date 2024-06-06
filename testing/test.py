from crewai import Agent , Task , Crew 
from langchain_community.chat_models import ChatOllama
from pydantic import BaseModel
from typing import List 


class NamedEntiies(BaseModel):
    city : List[str]
    country : List[str] 
    state : List[str]

    

model = ChatOllama(model='llama3' , temperature=0)

# general_agent = Agent(role = "Math Professor",
#                       goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
#                       backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
#                       allow_delegation = False,
#                       verbose = True,
#                       llm = model)

goal = """
Identify the city in the given sentence
If there is country or state name but not city name then respond the country's or state's capital city name 
NOTE : Output only the city name in one word or two words and nothing else.
If there are multiple cities respond with comma seperated city names
If the there is no place to mention then respond with None word and nothing else
"""

labels = ['city' , 'country' , 'state']

# print(help(Agent))

agent = Agent(
            role = "NER agent for city , state and country identification which is used to call APIs" ,
            goal = """Identify the named entities""" , 
            backstory = f"""You are an expert in Natural Language Processing. Your task is to identify common Named Entities (NER) in a given text.
The possible common Named Entities (NER) types are exclusively: ({", ".join(labels)}). Make sure to not provide any explanation for your response""",
            allow_delegation = False , 
                      verbose = True,
                      llm = model , max_iter =1)



description = """ Explain me about the weather today in chennai and vellore"""

output_format = """\
Repond with only a json object as the format below with non explanation 
{
city : [] , 
state : [] , 
country : []
}
"""
task = Task(description=description , 
                    expected_output = output_format , # 'Only respond with a JSON object and nothing else', 
                    agent = agent )

crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

print(result)