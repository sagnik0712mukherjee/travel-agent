from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

@tool("DuckDuckGoSearch")
def search_tool(query: str):
    """Search the web for information using DuckDuckGo."""
    return DuckDuckGoSearchRun().run(query)