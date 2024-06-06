from langchain_core.output_parsers import JsonOutputParser , StrOutputParser
from models import QueryAgentDataParser  , TimeData
from langchain_core.prompts import PromptTemplate
from datetime import datetime



class EntityExtractorAgent : 
    def __init__(self , llm) -> None:
        self.llm = llm
        self.parser = JsonOutputParser(pydantic_object=QueryAgentDataParser)
        self.prompt = prompt = PromptTemplate(
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
        partial_variables={"format_instructions": self.parser.get_format_instructions()},
    )

    def extract_entity(self , query) : 
        try :
            chain = self.prompt | self.llm | self.parser
            result = chain.invoke({"query":query})
            return result 
        except Exception as e :
            # print(e)
            print("Error in entity extraction")
            print("-" * 30)

class TimeExtractorAgent : 
    def __init__(self , llm) -> None  :
        self.llm = llm 
        self.parser  = JsonOutputParser(pydantic_object = TimeData)
        self.prompt =PromptTemplate(
            template ="""
            Identify the range of dates mentioned in the query given todays date : {today_date} 
            Reply with only the date range 
            If only one day is given then mention that one date 
            {format_instructions}
            Dates : {list_of_times}
            """,
        input_variables = ["list_of_times"] , 
        partial_variables= {"today_date" : str(datetime.now()),'format_instructions' : self.parser.get_format_instructions()}
        )
    
    def get_time_data(self , list_of_times ) : 
        chain = self.prompt | self.llm | self.parser
        result = chain.invoke({"list_of_times" : list_of_times})
        return result
    

class ChitChatAgent : 
    def __init__(self , llm )->None : 
        self.llm  = llm 
        self.parser = StrOutputParser() 
        self.prompt = PromptTemplate(
            template="""\
                You are a Weather Assistant who's goal is to be humourous to user and the user is trying to chit chat with you,
                Keep the user entertained by chating with user in a humourous and sarcastic tone
                Make sure your reply is suitable for both kids as well as adults 

                User : {query} 
            """ , 
            input_variables= ['query'] 
        )
    def chat(self , query ) : 
        chain = self.prompt | self.llm | self.parser 
        result = chain.invoke({"query" : query})
        # print(result)
        return result 


class HumourousAgent : 
    def __init__(self , llm) -> None:
        self.llm = llm
        self.parser = StrOutputParser() 
        self.prompt = PromptTemplate(template  = """\
                                     You are an incredibly wise, smart, witty and humours knowlegable weather announcement assistant
                                     % RESPONSE TONE:
                                     - Your response should have humor, sarcasm and should tease the reader. Make sure your response is suitable for adults and kids and don't discriminate

                                     % RESPONSE FORMAT:
                                     - Respond in under 200 characters
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
        
    def chat(self , query , context) :
        chain = self.prompt  | self.llm | self.parser 
        return chain.invoke({'query' : query , 'context' : context})