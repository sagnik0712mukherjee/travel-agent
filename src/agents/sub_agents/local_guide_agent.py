from crewai import Agent
from src.tools.search_tool import search_tool
from config.settings import llm_model

def get_local_guide_agent():

    local_guide = Agent(
        role='Local Tour Guide',
        goal='Provide the BEST insights about the selected city',
        backstory='A knowledgeable local guide with extensive information about the city, its attractions, and customs.',
        verbose=True,
        allow_delegation=False,
        llm=llm_model,
        tools=[search_tool]
    )

    return local_guide