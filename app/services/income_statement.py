import yfinance as yf
import numpy as np

def analyze_income_statement(stock: yf.Ticker):
    """
    Analyzes an income statement DataFrame, returning detailed financial performance metrics.

    Parameters:
    - df: DataFrame with income statement data (e.g., from yfinance stock.financials), with years as columns.

    Returns:
    - dict: Detailed income statement analysis including metrics, ratios, trends, and health summary.
    """
    try:
        # Validate DataFrame
        df = stock.income_stmt
        if df.empty or df.columns.empty:
            return {"error": "[Income Statement] DataFrame is empty or has no columns.", "module": "income_statement_analysis"}

        # Get years from column timestamps
        years = sorted([str(col.year) for col in df.columns], reverse=True)
        if not years:
            return {"error": "[Income Statement] No valid years found in data.", "module": "income_statement_analysis"}

        # Initialize output dictionary
        analysis = {
            "Metrics": {},
            "Ratios": {},
            "Trends": {},
        }

        # Define key income statement items to extract
        income_items = [
            "Total Revenue",
            "Operating Revenue",
            "Net Income",
            "Net Income From Continuing Operations",
            "Pretax Income",
            "Tax Provision",
            "Interest Expense",
            "Interest Income",
            "Net Interest Income",
            "Selling General And Administration",
            "Reconciled Depreciation",
            "Depreciation And Amortization In Income Statement",
            "Total Unusual Items",
            "Diluted EPS",
            "Basic EPS",
            "Diluted Average Shares",
            "Cash Dividends Paid"
        ]

        # Map years to actual column timestamps
        year_to_timestamp = {str(col.year): col for col in df.columns}

        # Extract metrics for each year
        for year in years:
            metrics = {}
            timestamp = year_to_timestamp.get(year)
            if not timestamp:
                metrics = {item: None for item in income_items}
            else:
                for item in income_items:
                    if item in df.index:
                        try:
                            value = float(df.loc[item, timestamp])
                            metrics[item] = value if not np.isnan(value) else None
                        except (KeyError, ValueError):
                            metrics[item] = None
                    else:
                        metrics[item] = None

            # Store metrics
            analysis["Metrics"][year] = metrics

            # Calculate ratios
            ratios = {}
            try:
                # Net Profit Margin (Net Income / Total Revenue)
                if metrics.get("Net Income") is not None and metrics.get("Total Revenue") is not None:
                    ratios["Net Profit Margin"] = (
                        metrics["Net Income"] / metrics["Total Revenue"] if metrics["Total Revenue"] != 0 else np.nan
                    )
                    ratios["Net Profit Margin"] = round(ratios["Net Profit Margin"], 2) if not np.isnan(ratios["Net Profit Margin"]) else None

                # Operating Margin (Pretax Income / Total Revenue)
                if metrics.get("Pretax Income") is not None and metrics.get("Total Revenue") is not None:
                    ratios["Operating Margin"] = (
                        metrics["Pretax Income"] / metrics["Total Revenue"] if metrics["Total Revenue"] != 0 else np.nan
                    )
                    ratios["Operating Margin"] = round(ratios["Operating Margin"], 2) if not np.isnan(ratios["Operating Margin"]) else None

                # Effective Tax Rate (Tax Provision / Pretax Income)
                if metrics.get("Tax Provision") is not None and metrics.get("Pretax Income") is not None:
                    ratios["Effective Tax Rate"] = (
                        abs(metrics["Tax Provision"]) / metrics["Pretax Income"] if metrics["Pretax Income"] != 0 else np.nan
                    )
                    ratios["Effective Tax Rate"] = round(ratios["Effective Tax Rate"], 2) if not np.isnan(ratios["Effective Tax Rate"]) else None

                # SG&A to Revenue (Selling General And Administration / Total Revenue)
                if metrics.get("Selling General And Administration") is not None and metrics.get("Total Revenue") is not None:
                    ratios["SG&A to Revenue"] = (
                        metrics["Selling General And Administration"] / metrics["Total Revenue"] if metrics["Total Revenue"] != 0 else np.nan
                    )
                    ratios["SG&A to Revenue"] = round(ratios["SG&A to Revenue"], 2) if not np.isnan(ratios["SG&A to Revenue"]) else None

                # Interest Coverage (Pretax Income / Interest Expense)
                if metrics.get("Pretax Income") is not None and metrics.get("Interest Expense") is not None:
                    ratios["Interest Coverage"] = (
                        metrics["Pretax Income"] / metrics["Interest Expense"] if metrics["Interest Expense"] != 0 else np.nan
                    )
                    ratios["Interest Coverage"] = round(ratios["Interest Coverage"], 2) if not np.isnan(ratios["Interest Coverage"]) else None

                # Dividend Payout Ratio (Cash Dividends Paid / Net Income)
                if metrics.get("Cash Dividends Paid") is not None and metrics.get("Net Income") is not None:
                    ratios["Dividend Payout Ratio"] = (
                        abs(metrics["Cash Dividends Paid"]) / metrics["Net Income"] if metrics["Net Income"] != 0 else np.nan
                    )
                    ratios["Dividend Payout Ratio"] = round(ratios["Dividend Payout Ratio"], 2) if not np.isnan(ratios["Dividend Payout Ratio"]) else None

            except ZeroDivisionError:
                ratios.update({
                    "Net Profit Margin": None,
                    "Operating Margin": None,
                    "Effective Tax Rate": None,
                    "SG&A to Revenue": None,
                    "Interest Coverage": None,
                    "Dividend Payout Ratio": None
                })

            analysis["Ratios"][year] = ratios


        # Convert dictionary keys to strings for JSON compatibility
        def convert_keys_to_str(d):
            if isinstance(d, dict):
                return {str(k): convert_keys_to_str(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [convert_keys_to_str(item) for item in d]
            else:
                return d

        return convert_keys_to_str(analysis)

    except Exception as e:
        return {"error": f"[Income Statement Analysis] {str(e)}", "module": "income_statement_analysis"}