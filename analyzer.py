def detect_trend(df):
    if df.empty or 'Close' not in df:
        return 'No data'

    latest = df['Close'].iloc[-1]
    past = df['Close'].iloc[0]

    if latest > past:
        return 'Uptrend'
    elif latest < past:
        return 'Downtrend'
    else:
        return 'Sideways'

def analyze(data):
    results = {}
    for symbol, df in data.items():
        trend = detect_trend(df)
        results[symbol] = trend
    return results
