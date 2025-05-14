from fetcher import fetch_market_data
from analyzer import analyze

def run():
    print("Fetching data...")
    data = fetch_market_data()
    print("Analyzing...")
    trends = analyze(data)

    for symbol, trend in trends.items():
        print(f"{symbol}: {trend}")

if __name__ == "__main__":
    run()
