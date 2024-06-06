from langchain.pydantic_v1 import BaseModel, Field , Extra , ValidationError 
from typing import List , Optional 
from datetime import datetime

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


class TimeData(BaseModel): 
    start_date : Optional[datetime] = Field(description="Date Time of start date")
    end_date : Optional[datetime] = Field(description="Date Time of end date")
    class Config : 
        extra = Extra.forbid
