from crewai import Crew
from app.agents.news_agent import news_analyst
from app.agents.financial_agent import financial_analyst
from app.agents.health_agent import financial_health_analyst
from app.agents.outlook_agent import investor_outlook_agent

from app.tasks.news_task import news_analysis_task
from app.tasks.financial_task import financial_analysis_task
from app.tasks.health_task import financial_health_analysis_task
from app.tasks.outlook_task import investor_outlook_task

def run_crew(ticker, company_name):
    crew = Crew(
        agents=[
            news_analyst,
            financial_analyst,
            financial_health_analyst,
            investor_outlook_agent
        ],
        tasks=[
            news_analysis_task,
            financial_analysis_task,
            financial_health_analysis_task,
            investor_outlook_task
        ],
        verbose=True
    )

    return crew.kickoff(
        inputs={
            "ticker": ticker,
            "company_name": company_name
        }
    )
