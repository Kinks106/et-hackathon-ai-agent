from crewai.tools import tool
from tavily import TavilyClient
import os

@tool
def web_search_tool(query: str) -> dict:
    """Search the web for stock-related information using Tavily and return structured results."""
    try:
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = tavily_client.search(query=query, search_depth="balanced", max_results=2)
        results = [
            {
                "title": res["title"],
                "url": res["url"],
                "content": res["content"][:800]  # Truncate to save tokens
            }
            for res in response["results"]
        ]
        return results
    except Exception as e:
        return {"error": f"Error during Tavily search: {str(e)}"}