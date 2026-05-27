import pandas as pd
import numpy as np
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
FEATURE_DIR = Path("data/features")

FEATURE_DIR.mkdir(parents=True, exist_ok=True)


def generate_features(ticker: str):

    input_path = PROCESSED_DIR / f"{ticker}.parquet"
    output_path = FEATURE_DIR / f"{ticker}.parquet"

    print(f"Generating features for {ticker}...")

    df = pd.read_parquet(input_path)

    # =========================
    # Returns
    # =========================

    df["returns"] = df["close"].pct_change()

    df["log_returns"] = np.log(
        df["close"] / df["close"].shift(1)
    )

    # =========================
    # Moving Averages
    # =========================

    df["sma_20"] = df["close"].rolling(20).mean()

    df["sma_50"] = df["close"].rolling(50).mean()

    df["ema_20"] = df["close"].ewm(span=20).mean()

    # =========================
    # Volatility
    # =========================

    df["rolling_vol_20"] = (
        df["returns"]
        .rolling(20)
        .std()
        * np.sqrt(252)
    )

    # =========================
    # Momentum
    # =========================

    df["momentum_10"] = (
        df["close"] / df["close"].shift(10)
    ) - 1

    # =========================
    # Bollinger Bands
    # =========================

    rolling_std = df["close"].rolling(20).std()

    df["bollinger_upper"] = (
        df["sma_20"] + 2 * rolling_std
    )

    df["bollinger_lower"] = (
        df["sma_20"] - 2 * rolling_std
    )

    # =========================
    # Relative Volume
    # =========================

    if "volume" in df.columns:

        volume_ma = df["volume"].rolling(20).mean()

        df["relative_volume"] = (
            df["volume"] / volume_ma
        )

    # Remove early NaNs from rolling windows
    df = df.dropna()

    # Save features
    df.to_parquet(output_path)

    print(f"Saved features -> {output_path}")


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
        generate_features(ticker)

    print("Feature engineering complete.")