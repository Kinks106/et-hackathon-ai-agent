from backend.services.fundamental_analysis import interpret_pe_ratio, interpret_price_to_book
import yfinance as yf

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(series, short_window=12, long_window=26, signal_window=9):
    short_ema = series.ewm(span=short_window, adjust=False).mean()
    long_ema = series.ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal

# --- Interpretations ---

def analyze_trend(latest):
    if latest['Close'] > latest['SMA_50'] > latest['SMA_200']:
        return "Bullish"
    elif latest['Close'] < latest['SMA_50'] < latest['SMA_200']:
        return "Bearish"
    else:
        return "Neutral"

def analyze_macd(latest):
    return "Bullish" if latest['MACD'] > latest['Signal'] else "Bearish"

def analyze_rsi(latest):
    if latest['RSI'] > 70:
        return "Overbought"
    elif latest['RSI'] < 30:
        return "Oversold"
    else:
        return "Neutral"

def analyze_bollinger_bands(latest):
    if latest['Close'] > latest['BB_Upper']:
        return "Price above upper band (Overbought)"
    elif latest['Close'] < latest['BB_Lower']:
        return "Price below lower band (Oversold)"
    else:
        return "Price within bands"
    
def get_technical_analysis(stock: yf.Ticker) -> dict:
    try:
        history = stock.history(period="1y")
        info = stock.info

        # Calculate indicators
        history['SMA_50'] = history['Close'].rolling(window=50).mean()
        history['SMA_200'] = history['Close'].rolling(window=200).mean()
        history['RSI'] = calculate_rsi(history['Close'])
        history['MACD'], history['Signal'] = calculate_macd(history['Close'])
        history['BB_Middle'] = history['Close'].rolling(window=20).mean()
        history['BB_Std'] = history['Close'].rolling(window=20).std()
        history['BB_Upper'] = history['BB_Middle'] + 2 * history['BB_Std']
        history['BB_Lower'] = history['BB_Middle'] - 2 * history['BB_Std']

        latest = history.iloc[-1]

        technical_analysis = {
            "Trend": analyze_trend(latest),
            "MACD Interpretation": analyze_macd(latest),
            "RSI Interpretation": analyze_rsi(latest),
            "Bollinger Bands": analyze_bollinger_bands(latest),
            "SMA_50": round(latest['SMA_50'], 2),
            "SMA_200": round(latest['SMA_200'], 2),
            "RSI": round(latest['RSI'], 2),
            "MACD": round(latest['MACD'], 2),
            "Signal": round(latest['Signal'], 2),
            "BB_Upper": round(latest['BB_Upper'], 2),
            "BB_Lower": round(latest['BB_Lower'], 2),
            "P/E Ratio Interpretation": interpret_pe_ratio(info.get('trailingPE')),
            "Price to Book Interpretation": interpret_price_to_book(info.get('priceToBook')),
        }

        return technical_analysis

    except Exception as e:
        return {"error": str(e)}