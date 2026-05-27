import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path("data/processed")


def validate_asset(ticker: str):

    path = PROCESSED_DIR / f"{ticker}.parquet"

    df = pd.read_parquet(path)

    print(f"\nValidating {ticker}")

    print("-" * 40)

    print(f"Rows: {len(df)}")

    print(f"Missing values:\n{df.isnull().sum()}")

    print(f"Duplicate timestamps: {df.index.duplicated().sum()}")

    print(f"Date range: {df.index.min()} -> {df.index.max()}")

    print(f"Columns: {list(df.columns)}")


if __name__ == "__main__":

    tickers = [
        "SPY",
        "QQQ",
        "AAPL",
        "MSFT",
        "JPM",
        "XOM"
    ]

    for ticker in tickers:
        validate_asset(ticker)