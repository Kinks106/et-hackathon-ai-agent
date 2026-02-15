import yfinance as yf
import numpy as np

def get_fundamental_analysis(stock: yf.Ticker) -> dict:
    try:
        history = stock.history(period='1y')
        info = stock.info

        fundamental_analysis = {
            "Name": info.get("longName", "N/A"),
            "Exchange": info.get("exchange", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "Open": info.get("open", "N/A"),
            "Day Low": info.get("dayLow", "N/A"),
            "Day High": info.get("dayHigh", "N/A"),
            "Previous Close": info.get("previousClose", "N/A"),
            "Current Price": info.get("currentPrice", "N/A"),
            "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
            "52 Week Change Percent": info.get("fiftyTwoWeekHighChangePercent", "N/A"),
            "52 Week Low Change Percent": info.get(
                "fiftyTwoWeekLowChangePercent", "N/A"
            ),
            "Average Volume": info.get("averageVolume", "N/A"),
            'PE Ratio': info.get('trailingPE', 'N/A'),
            'Forward PE': info.get('forwardPE', 'N/A'),
            'Price to Book': info.get('priceToBook', 'N/A'),
            'Dividend Yield': info.get('dividendYield', 'N/A'),
            'EPS (TTM)': info.get('trailingEps', 'N/A'),
            'Revenue Growth': info.get('revenueGrowth', 'N/A'),
            'Return on Equity': info.get('returnOnEquity', 'N/A'),
            'Operating Margin': info.get('operatingMargins', 'N/A'),
            'Earnings Growth': info.get('earningsGrowth', 'N/A'),
            'Book Value': info.get('bookValue', 'N/A'),
            'Operating Cash Flow': info.get('operatingCashflow', 'N/A'),
            'Return on Assets': info.get('returnOnAssets', 'N/A'),
            'Stock Price Avg (Period)': history['Close'].mean(),
            'Stock Price Max (Period)': history['Close'].max(),
            'Stock Price Min (Period)': history['Close'].min()
        }

        return fundamental_analysis

    except Exception as e:
        return {"error": str(e)}
    
def interpret_pe_ratio(pe):
    if pe is None or pe == 'N/A':
        return "Data not available"
    if pe < 15:
        return "Undervalued"
    elif pe > 30:
        return "Overvalued"
    else:
        return "Fairly Valued"

def interpret_price_to_book(pb):
    if pb is None or pb == 'N/A':
        return "Data not available"
    if pb < 1:
        return "Undervalued"
    elif pb > 3:
        return "Overvalued"
    else:
        return "Fairly Valued"