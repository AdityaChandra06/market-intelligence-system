import pandas as pd
import numpy as np
from pathlib import Path

FEATURE_DIR = Path("data/features")
REGIME_DIR = Path("data/regimes")

REGIME_DIR.mkdir(parents=True, exist_ok=True)


def label_regimes(ticker: str):

    input_path = FEATURE_DIR / f"{ticker}.parquet"
    output_path = REGIME_DIR / f"{ticker}.parquet"

    print(f"Labeling regimes for {ticker}...")

    df = pd.read_parquet(input_path)

    # =========================
    # Trend Signal
    # =========================

    df["trend_signal"] = (
        df["sma_20"] - df["sma_50"]
    )

    # =========================
    # Rolling Max for Drawdown
    # =========================

    rolling_max = df["close"].cummax()

    df["drawdown"] = (
        df["close"] - rolling_max
    ) / rolling_max

    # =========================
    # Initialize Regime Column
    # =========================

    df["regime"] = "sideways"

    #=========================
    #Sideways Regime
    #=========================

    sideways_condition = (
        (abs(df["trend_strength"]) < 0.01)
        &
        (df["rolling_vol_20"] < 0.25)
    )

    df.loc[sideways_condition, "regime"] = "sideways"


    # =========================
    # Bear Regime
    # =========================

    bear_condition = (
        (df["trend_signal"] < -0.1) &
        (df["rolling_vol_20"] > 0.20)
    )

    df.loc[bear_condition, "regime"] = "bear"

    # =========================
    # Panic Regime
    # =========================

    panic_condition = (
        (df["rolling_vol_20"] > 0.35)
        &
        (df["drawdown"] < -0.20)
        &
        (df["momentum_10"] < -0.10)
    )

    df.loc[panic_condition, "regime"] = "panic"

    

    # =========================
    # Bull Regime
    # =========================

    bull_condition = (
        (df["trend_signal"] > 0.0) &
        (df["rolling_vol_20"] < 0.3)
    )

    df.loc[bull_condition, "regime"] = "bull"

    # =========================
    # Regime Encoding
    # =========================

    regime_mapping = {
        "sideways": 0,
        "bull": 1,
        "bear": 2,
        "panic": 3
    }

    df["regime_code"] = (
        df["regime"]
        .map(regime_mapping)
    )

    # Save regime dataset
    df.to_parquet(output_path)

    print(f"Saved regimes -> {output_path}")



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
        label_regimes(ticker)

    print("Regime labeling complete.")