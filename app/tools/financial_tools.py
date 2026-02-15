from typing import Dict, Any
import yfinance as yf
from crewai.tools import tool 
from app.services.balance_sheet import analyze_balance_sheet
from app.services.income_statement import analyze_income_statement
from app.services.fundamental_analysis import get_fundamental_analysis
from app.services.technical_analysis import get_technical_analysis
from app.services.risk_analysis import get_risk_assessment

@tool
def financial_health_data(ticker: str) -> Dict[str, Any]:
    """
    Fetch stock data, income statement, and historical prices for the given ticker,
    and sanitize output for JSON compatibility.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL").

    Returns:
        dict: JSON-safe financial data dictionary.
    """
    try:
        stock = yf.Ticker(ticker)
        balance_sheet_data = analyze_balance_sheet(stock)
        income_statement_data = analyze_income_statement(stock)
        data = {
            "balance_sheet_data" : balance_sheet_data,
            "income_statement_data" : income_statement_data,
        }

        return data

    except Exception as e:
        return {"error": str(e)}

@tool
def financial_analysis_data(ticker: str) -> Dict[str, Any]:
    """
    Fetch stock data, income statement, and historical prices for the given ticker,
    and sanitize output for JSON compatibility.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL").

    Returns:
        dict: JSON-safe financial data dictionary.
    """
    try:
        stock = yf.Ticker(ticker)
        fundamental_analysis = get_fundamental_analysis(stock)
        technical_analysis = get_technical_analysis(stock)
        risk_analysis = get_risk_assessment(stock)
        data = {
            "fundamental_analysis" : fundamental_analysis,
            "technical_analysis" : technical_analysis,
            "risk_analysis" : risk_analysis
        }

        return data

    except Exception as e:
        return {"error": str(e)}
