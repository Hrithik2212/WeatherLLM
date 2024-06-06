from crewai import Agent , Task , Crew 
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model='gemma:2b')

general_agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
                      allow_delegation = False,
                      verbose = True,
                      llm = model)
task = Task (description="""what is integratiion of (cos^2 theta + sin^2) theata""",
             expected_output='One Word Answer',
             agent = general_agent)

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

print(result)


agent = Agent(
            role = "NER agent for city Identification" ,
            goal =\
"""
Identify the city in the given sentence
If there is country or state name but not city name then respond the country's or state's capital city name 
NOTE : Output only the city name in one word or two words and nothing else.
If there are multiple cities respond with comma seperated city names
If the there is no place to mention then respond with None word and nothing else
""" ,
            backstory = "The response given by you will be directly used to get the coordinates of the city with the help of an API" ,
            allow_delegation = False , 
                      verbose = True,
                      llm = model )

description = "How is it in chennai"
task = Task(description=description , 
                    expected_output = "Respond with the name of the city or None if no city or place is mentioned")

crew = Crew(agents=[agent] , 
            tasks=[task], verbose =2 )

print(crew.kickoff())