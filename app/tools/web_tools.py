from crewai.tools import tool
import tavily

@tool
def web_search_tool(query: str) -> dict:
    """Search the web for stock-related information using Tavily and return structured results."""
    try:
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        results = [
            {
                "title": res["title"],
                "url": res["url"],
                "content": res["content"]
            }
            for res in response["results"]
        ]
        return results
    except Exception as e:
        return {"error": f"Error during Tavily search: {str(e)}"}