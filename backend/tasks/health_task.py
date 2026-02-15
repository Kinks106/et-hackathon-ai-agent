from crewai import Task
from backend.schemas.health_schema import FinancialHealthReport
from backend.agents.health_agent import financial_health_analyst


financial_health_analysis_task = Task(
    description=(
        "Use the `financial_health_data` tool to retrieve the company's balance sheet and income statement for {ticker}. "
        "Analyze the data to assess the company's financial stability and operational efficiency.\n\n"

        "Provide a detailed assessment of:\n"
        "- **Balance Sheet**: Liquidity, solvency, and debt levels.\n"
        "- **Income Statement**: Revenue trends, profit margins, and earnings quality.\n\n"

        "Conclude with a final `verdict` on the company's overall financial health (Strong/Stable/Weak) and a brief outlook."
    ),
    agent=financial_health_analyst,
    inputs=["ticker"],
    expected_output="A JSON object matching the FinancialHealthReport schema, with balance_sheet, income_statement, and verdict.",
    output_pydantic=FinancialHealthReport
)