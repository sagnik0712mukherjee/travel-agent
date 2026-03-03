from crewai import Crew
from src.tasks.city_plan import get_city_plan_task
from src.tasks.guide_plan import get_guide_plan_task
from src.tasks.travel_plan import get_travel_plan_task
from src.agents.sub_agents.city_agent import get_city_agent
from src.agents.sub_agents.local_guide_agent import get_local_guide_agent

def build_crew_agent(from_city, destination_city, start_date, end_date, hobbies):

    city_expert = get_city_agent()
    local_guide = get_local_guide_agent()

    city_task = get_city_plan_task(from_city, destination_city, start_date, end_date)
    guide_task = get_guide_plan_task(destination_city, start_date, end_date, hobbies)
    travel_task = get_travel_plan_task()

    crew = Crew(
        agents=[city_expert, local_guide],
        tasks=[city_task, guide_task, travel_task],
        verbose=True
    )

    return crew