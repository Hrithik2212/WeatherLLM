from crewai import Task
from testing.agents import * 

class HumourousWeatherBotTasks():
    def __init__(self ,verbose =True):
        self.verbose = verbose

    def city_entity_recognition(self , query ):
        description = query 
        task = Task(description=description , 
                    expected_output = "Respond with the name of the city or None if no city or place is mentioned")
        return task 

    def get_time_range(self, query) :
        description = query 
        task = Task(description=description,
                    expected_output = """\
The output you give should be a None or json format as follows
{
"response" : {
forecast : "True" ,
history : "False"
dates : "22-12-2023 - 01-01-2024"   
}
}
""")  