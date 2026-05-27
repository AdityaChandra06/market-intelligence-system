import yfinance as yf
import pandas as pd
from pathlib import Path

#Assets to download:

TICKERS={
    "SPY",
    "QQQ",
    "AAPL",
    "MSFT",
    "JPM",
    "XOM"   
}

#Data storange path:

DATA_DIR=Path("data/raw")

#Make directory if it doesnt exist

DATA_DIR.mkdir(parents=True, exist_ok=True)

#Download and save assets:

for ticker in TICKERS:
    print(f"Downloading data for {ticker}...")

    df=yf.download(ticker, start="2000-01-01", auto_adjust=True)
    df.columns = [col[0].lower() for col in df.columns]

    output_path=DATA_DIR / f"{ticker}.parquet"
    df.to_parquet(output_path)
    print(f"Saved {ticker} data to {output_path}")
print("All data downloaded and saved successfully.")