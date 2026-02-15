from crewai import Crew
from backend.agents.news_agent import news_analyst
from backend.agents.financial_agent import financial_analyst
from backend.agents.health_agent import financial_health_analyst
from backend.agents.outlook_agent import investor_outlook_agent

from backend.tasks.news_task import news_analysis_task
from backend.tasks.financial_task import financial_analysis_task
from backend.tasks.health_task import financial_health_analysis_task
from backend.tasks.outlook_task import investor_outlook_task

import time

def rate_limit_sleeper(output):
    """Sleep after each task to avoid hitting Groq's RPM/TPM limits."""
    print("\n[Rate Limit Guard] Sleeping for 70s to FULLY reset API token quota...\n")
    time.sleep(70)

def run_crew(ticker, company_name):
    # Dynamically attach the sleep callback to avoid modifying every task file
    tasks = [
        news_analysis_task,
        financial_analysis_task,
        financial_health_analysis_task,
        investor_outlook_task
    ]

    # Attach callback to all tasks except the last one (no need to sleep after the final task)
    for i, task in enumerate(tasks[:-1]):
        task.callback = rate_limit_sleeper

    crew = Crew(
        agents=[
            news_analyst,
            financial_analyst,
            financial_health_analyst,
            investor_outlook_agent
        ],
        tasks=tasks,
        verbose=True
    )

    return crew.kickoff(
        inputs={
            "ticker": ticker,
            "company_name": company_name
        }
    )
