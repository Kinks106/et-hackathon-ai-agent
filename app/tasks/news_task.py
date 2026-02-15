from crewai import Task
from app.schemas.news_schema import NewsSentimentAnalysis
from app.agents.news_agent import news_analyst

news_analysis_task = Task(
    description = (
    "Use the `web_search_tool` **only once and only at the beginning** of your reasoning process. "
    "Pass exactly one string to the tool in the format `'{company_name} latest news' or {company_name} market-moving news`. "

    "After retrieving the articles, analyze each individually for sentiment (Positive, Neutral, or Negative) "
    "based on tone, bias, and its likely influence on market perception.\n\n"

    "For each article, return:\n"
    "- Title\n"
    "- 2–3 line summary\n"
    "- Sentiment (Positive, Neutral, Negative)"
    "- 2–5 key points or takeaways\n"

    "Then, assign a `sentiment_score` between 0 (very negative) and 10 (very positive), "
    "based on the aggregate tone and impact of all articles.\n\n"

    "Finally, provide a 5–10 line investment insight or recommendation based on the overall sentiment pattern.\n\n"

    "**Important: You are allowed to call `web_search_tool` only once. Do not attempt another call or retry.**"
),
    agent=news_analyst,
    expected_output=(
        "Return a structured `NewsSentimentAnalysis`"
    ),
    output_pydantic=NewsSentimentAnalysis
)
