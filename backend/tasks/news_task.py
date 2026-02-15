from crewai import Task
from backend.schemas.news_schema import NewsSentimentAnalysis
from backend.agents.news_agent import news_analyst

news_analysis_task = Task(
    description = (
    "You MUST use the tool named `web_search_tool`. \n"
    "DO NOT try to use `brave_search` or `google_search`. They do not exist.\n"
    "Use `web_search_tool` to search for the latest news about {company_name} ({company_name} market-moving news). "
    "Analyze the retrieved articles for sentiment (Positive, Neutral, or Negative), tone, and potential market impact.\n\n"

    "For each relevant article, extract:\n"
    "- Title\n"
    "- High-level summary\n"
    "- Key takeaways\n"
    "- Sentiment assessment\n\n"

    "Finally, provide an overall `sentiment_score` (0-10) and a strategic investment insight based on the aggregated news.\n\n"

    "**CRITICAL:** Do NOT call any other tools to return the result. Just return the valid JSON object as your final answer."
),
    agent=news_analyst,
    expected_output=(
        "Return a structured `NewsSentimentAnalysis`"
    ),
    output_pydantic=NewsSentimentAnalysis
)
