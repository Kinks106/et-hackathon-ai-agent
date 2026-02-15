from crewai import Task
from app.schemas.health_schema import FinancialHealthReport
from app.agents.health_agent import financial_health_analyst


financial_health_analysis_task = Task(
    description=(
        "Use the `financial_health_data` tool **only once** and input only the stock {ticker} (e.g., 'AAPL', 'MSFT') as a plain string. "
        "The tool will return the company's balance sheet and income statement data.\n\n"

        "Analyze both sections separately:\n"
        "- **Balance Sheet**: Assess liquidity, short-term obligations, and solvency ratios.\n"
        "- **Income Statement**: Analyze revenue, profitability, margins, and earnings growth.\n\n"

        "For each section, provide:\n"
        "- A 4–5 line summary\n"
        "- Include 3 to 10 bullet-pointed insights drawn from the data"
        "- An `ai_score` between 0 and 10 representing the strength of that section\n\n"

        "Conclude with a one-line `verdict` summarizing the company's overall financial health and outlook for investors."
    ),
    agent=financial_health_analyst,
    inputs=["ticker"],
    expected_output=(
        "A structured `FinancialHealthReport` object containing:\n"
        "- `balance_sheet`: HealthSection\n"
        "- `income_statement`: HealthSection\n"
        "- `verdict`: Summary recommendation"
    ),
    output_pydantic=FinancialHealthReport
)