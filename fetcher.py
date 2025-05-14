import yfinance as yf
from config import MARKET_SYMBOLS, DAYS_LOOKBACK
from datetime import datetime, timedelta

def fetch_market_data():
    end = datetime.today()
    start = end - timedelta(days=DAYS_LOOKBACK)
    data = {}

    for symbol in MARKET_SYMBOLS:
        stock = yf.download(symbol, start=start, end=end)
        data[symbol] = stock

    return data
