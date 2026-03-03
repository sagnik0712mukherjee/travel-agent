from crewai import Task
from src.agents.sub_agents.city_agent import get_city_agent
from config.settings import data_folder

city_expert = get_city_agent()
def get_travel_plan_task():

    travel_plan_task = Task(
        description='Summarize the city plan and the guide plan into a single cohesive travel document.',
        agent=city_expert,
        expected_output='A summarized travel plan combining city details and daily itinerary.',
        output_file=f'{data_folder}/travel.md'
    )

    return travel_plan_task