from crewai import Agent 

class HumourousWeathorBotAgents():
    def __init__(self , llm , verbose = True):
        self.llm = llm 
        self.verbose = verbose 

    def create_place_retrieval_agent(self ):
        agent = Agent(
            role = "NER agent for city" ,
            goal =\
"""
Identify the city in the given sentence
If there is country or state name but not city name then respond the country's or state's capital city name 
NOTE : Output only the city name in one word or two words and nothing else.
If there are multiple cities respond with comma seperated city names
If the there is no place to mention then respond with None word and nothing else
""" ,
            backstory = "The response given by you will be directly used to get the coordinates of the city with the help of an API" ,
            allow_delegations = False ,
            verbose = self.verbose ,
            llm = self.llm 
        )
        return agent 
    
    def create_time_retrievel_agent(self ):
        agent = Agent(role = "Forecaster assistant" , 
                      goal =\
"""
Given a sentence , You have to identify wether the customer wants you to forecast or not and if yes mention the number of date he wants forecast on in DD-MM-YYYY format.
If the custmoer wants forecast between the number of days then respond with the format of DD-MM-YYYY - DD-MM-YYYY .
If the customer didn't mention any forecast but wants historical data then return the days or range of days he wants the historical data,
Return None otherwise
"""  ,
                      backstory = "The response given by you will be directly used to call a weather API" ,
                      allow_delegations = False ,
                      verbose = self.verbose ,
                      llm = self.llm 
                    )
        return agent
