from crewai import Task
from src.agents.sub_agents.local_guide_agent import get_local_guide_agent
from config.settings import data_folder

local_guide = get_local_guide_agent()
def get_guide_plan_task(destination_city, start_date, end_date, hobbies):

    guide_plan_task = Task(
        description=f'Create a detailed daily itinerary for a trip to {destination_city} from {start_date} to {end_date}, considering the user has interests in: {hobbies}. Include specific places to visit and food recommendations.',
        agent=local_guide,
        expected_output='A day-by-day itinerary tailored to user interests.',
        output_file=f'{data_folder}/guide_plan.md'
    )

    return guide_plan_task