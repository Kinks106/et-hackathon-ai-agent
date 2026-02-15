from app.tools.web_tools import web_search_tool
from crewai import Agent
from app.llms.models import groq_llama_70b



news_analyst = Agent(
    role = "News Analysis Agent",
    goal = '''Analyze news articles for relevance, sentiment, key insights, and potential market impact to support strategic
    and financial decision-making.''',
    backstory = '''You are a seasoned news analyst with deep expertise in financial and corporate reporting.
    Your job is to extract meaningful insights, assess sentiment, and evaluate potential implications
    for companies, sectors, or markets to support informed decision-making.''',
    max_rpm=2,
    max_iter=5,
    llm = groq_llama_70b,
    tools=[web_search_tool],
)