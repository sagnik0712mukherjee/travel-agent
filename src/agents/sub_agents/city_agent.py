from crewai import Agent
from src.tools.search_tool import search_tool
from config.settings import llm_model

def get_city_agent():

    city_expert = Agent(
        role='City Selection Expert',
        goal='Select the best combinations/results based on weather, season, and prices',
        backstory='An expert in analyzing travel data to pick the best destinations.',
        verbose=True,
        allow_delegation=False,
        llm=llm_model,
        tools=[search_tool]
    )

    return city_expert