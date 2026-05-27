import pandas as pd
import numpy as np
from pathlib import Path

FEATURE_DIR = Path("data/features")
VOL_DIR = Path("data/volatility")

VOL_DIR.mkdir(parents=True, exist_ok=True)

def generate_volatility_targets(ticker: str):
    input_path = FEATURE_DIR / f"{ticker}.parquet"
    output_path = VOL_DIR / f"{ticker}.parquet"

    print(f"Generating volatility targets for {ticker}...")

    df = pd.read_parquet(input_path)

    # =========================
    # Future 5 day Volatility
    # =========================

    future_returns= df["returns"].shift(-1)
    df["future_vol_5d"] = (
        future_returns.rolling(5).std() * np.sqrt(252))
    
    # =========================
    # Future 10 day Volatility
    # =========================

    df["future_vol_10d"] = (
        future_returns.rolling(10).std() * np.sqrt(252))
    
    # =========================
    # Volatility expansion target
    # =========================

    df["vol_expansion"] = (df["future_vol_5d"] > df["rolling_vol_20"]).astype(int)

    #Dropping NaNs

    df = df.dropna()

    #Saving the DataFrame

    df.to_parquet(output_path, index=False)
    print(f"Saved volatility targets -> {output_path}")

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
        generate_volatility_targets(ticker)

    print("Volatility target generation complete.")