import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_asset(ticker: str):

    input_path = RAW_DIR / f"{ticker}.parquet"
    output_path = PROCESSED_DIR / f"{ticker}.parquet"

    print(f"Cleaning {ticker}...")

    # Load raw data
    df = pd.read_parquet(input_path)

    # Remove duplicate timestamps
    df = df[~df.index.duplicated(keep="first")]

    # Sort index
    df = df.sort_index()

    # Drop rows with missing OHLC data
    df = df.dropna(subset=["open", "high", "low", "close"])

    # Remove negative prices
    df = df[
        (df["open"] > 0) &
        (df["high"] > 0) &
        (df["low"] > 0) &
        (df["close"] > 0)
    ]

    # Forward fill volume if missing
    if "volume" in df.columns:
        df["volume"] = df["volume"].fillna(0)

    # Save cleaned data
    df.to_parquet(output_path)

    print(f"Saved cleaned data -> {output_path}")


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
        clean_asset(ticker)

    print("Cleaning pipeline complete.")