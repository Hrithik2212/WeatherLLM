from testing.tasks import * 
from testing.agents import * 
from weather_functions import * 
from crewai import Crew
from langchain_community.chat_models import ChatOllama



llm_model = ChatOllama(model="llama3")
Agents = HumourousWeathorBotAgents(llm=llm_model)
tasks = HumourousWeatherBotTasks()


def retrieve_place(query ) :
    agent = Agents.create_place_retrieval_agent()
    task = tasks.city_entity_recognition(query=query)
    date_retrieval_crew = Crew(agents = [agent] , task = [task] , verbose=2 )
    response = date_retrieval_crew.kickoff()
    print(response)
    return response


def main():
    query = "How is it in chennai"
    print(retrieve_place(query))


if __name__ == "__main__":
    main()