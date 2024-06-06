from pydantic import BaseModel, Field , ValidationError 
from typing import List , Tuple , Optional


class UserQueryModel(BaseModel):
    query : str = Field(description="The query sent by the user")
    default_city : Optional[str] = Field(description="City at which the user wants to query at")
    widget_city : Optional[str] = Field(description='City set at the Weather widget')

class WidgetData(BaseModel) : 
    widget_city: str = Field(description="City selected or defaulted from the city") 
