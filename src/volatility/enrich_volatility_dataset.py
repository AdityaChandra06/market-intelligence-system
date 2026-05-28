import pandas as pd
from pathlib import Path

# ======================================
# Directories
# ======================================

REGIME_DIR = Path("data/regimes")
VOL_DIR = Path("data/volatility")

# ======================================
# Columns To Transfer
# ======================================

COLUMNS_TO_ADD = [
    "drawdown",
    "regime",
    "regime_code"
]

# ======================================
# Enrichment Function
# ======================================

def enrich_volatility_dataset(ticker: str):

    regime_path = REGIME_DIR / f"{ticker}.parquet"
    vol_path = VOL_DIR / f"{ticker}.parquet"

    print(f"\nEnriching {ticker} volatility dataset...")

    # Load datasets
    regime_df = pd.read_parquet(regime_path)

    vol_df = pd.read_parquet(vol_path)

    # ======================================
    # Copy Columns From Regime Dataset
    # ======================================

    for column in COLUMNS_TO_ADD:

        if column not in regime_df.columns:
            print(f"Missing column in regime data: {column}")
            continue

        # Align using index
        vol_df[column] = regime_df[column]

    # ======================================
    # Drop rows with missing values
    # ======================================

    vol_df = vol_df.dropna()

    # ======================================
    # Save updated volatility dataset
    # ======================================

    vol_df.to_parquet(vol_path)

    print(f"Updated volatility dataset saved -> {vol_path}")


# ======================================
# Run Pipeline
# ======================================

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
        enrich_volatility_dataset(ticker)

    print("\nVolatility dataset enrichment complete.")