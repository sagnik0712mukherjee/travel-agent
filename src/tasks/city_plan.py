from crewai import Task
from src.agents.sub_agents.city_agent import get_city_agent
from config.settings import data_folder

city_expert = get_city_agent()
def get_city_plan_task(from_city, destination_city, start_date, end_date):

    city_plan_task = Task(
        description=f'Analyze and provide a detailed guide for a trip from {from_city} to {destination_city} from {start_date} to {end_date}. Include weather, travel routes, and general tips.',
        agent=city_expert,
        expected_output='A comprehensive city guide including weather, travel routes, and tips.',
        output_file=f'{data_folder}/city_plan.md'
    )

    return city_plan_task