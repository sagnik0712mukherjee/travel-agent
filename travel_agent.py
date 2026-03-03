import streamlit as st
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOpenAI
import os

from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# Set page title
st.title("Travel Agent with CrewAI")

# Streamlit App Title
st.title("AI-Powered Trip Planner")
st.markdown ("""
**Plan your next trip with AI!**\n
Enter your travel details below,
and our AI-powered travel assistant will create a personalized plan for you!
Best places to visit,
Accommodation & budget planning,
Local food recommendations,
Transportation & visa details,
and a lot more...
""")

# Input fields
from_city = st.text_input("From City")
destination_city = st.text_input("Destination City")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
hobbies = st.text_area("Hobbies/Interests")

if st.button("Generate Plan"):
    if not from_city or not destination_city or not start_date or not end_date:
        st.error("Please fill in all fields.")
    else:
        with st.spinner("Generating your travel plan... This may take a while."):
            try:
                # Initialize LLM
                api_key = os.environ.get("OPENAI_API_KEY")
                if not api_key:
                    st.error("OPENAI_API_KEY not found in environment variables.")
                    st.stop()
                
                llm = ChatOpenAI(api_key=api_key, model_name="gpt-4o-mini")

                # Initialize Search Tool
                @tool("DuckDuckGoSearch")
                def search_tool(query: str):
                    """Search the web for information using DuckDuckGo."""
                    return DuckDuckGoSearchRun().run(query)

                # Define Agents
                city_expert = Agent(
                    role='City Selection Expert',
                    goal='Select the best city based on weather, season, and prices',
                    backstory='An expert in analyzing travel data to pick the best destinations.',
                    verbose=True,
                    allow_delegation=False,
                    llm=llm,
                    tools=[search_tool]
                )

                local_guide = Agent(
                    role='Local Tour Guide',
                    goal='Provide the BEST insights about the selected city',
                    backstory='A knowledgeable local guide with extensive information about the city, its attractions, and customs.',
                    verbose=True,
                    allow_delegation=False,
                    llm=llm,
                    tools=[search_tool]
                )

                # Define Tasks
                task1 = Task(
                    description=f'Analyze and provide a detailed guide for a trip from {from_city} to {destination_city} from {start_date} to {end_date}. Include weather, travel routes, and general tips.',
                    agent=city_expert,
                    expected_output='A comprehensive city guide including weather, travel routes, and tips.',
                    output_file='city_plan.md'
                )

                task2 = Task(
                    description=f'Create a detailed daily itinerary for a trip to {destination_city} from {start_date} to {end_date}, considering the user has interests in: {hobbies}. Include specific places to visit and dining recommendations.',
                    agent=local_guide,
                    expected_output='A day-by-day itinerary tailored to user interests.',
                    output_file='guide_plan.md'
                )
                
                task3 = Task(
                    description='Summarize the city plan and the guide plan into a single cohesive travel document.',
                    agent=city_expert, # Reusing city expert for summary or could create a new one
                    expected_output='A summarized travel plan combining city details and daily itinerary.',
                    output_file='travel.md'
                )

                # Create Crew
                crew = Crew(
                    agents=[city_expert, local_guide],
                    tasks=[task1, task2, task3],
                    verbose=True
                )

                # Execute Crew
                result = crew.kickoff()

                st.success("Plan Generated Successfully!")
                
                st.subheader("Travel Plan Summary")
                st.markdown(result)

                # Option to display individual files if needed
                if os.path.exists('city_plan.md'):
                    with st.expander("View City Plan"):
                        with open('city_plan.md', 'r') as f:
                            st.markdown(f.read())
                
                if os.path.exists('guide_plan.md'):
                    with st.expander("View Guide Plan"):
                        with open('guide_plan.md', 'r') as f:
                            st.markdown(f.read())
                            
                if os.path.exists('travel.md'):
                     with st.expander("View Full Travel Document"):
                        with open('travel.md', 'r') as f:
                            st.markdown(f.read())

            except Exception as e:
                st.error(f"An error occurred: {e}")
