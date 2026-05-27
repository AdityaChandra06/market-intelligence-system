import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

def load_asset(ticker: str) -> pd.DataFrame:
    path = DATA_DIR / f"{ticker}.parquet"

    if not path.exists():
        raise FileNotFoundError(f"{ticker} data not found.")

    df = pd.read_parquet(path)

    return df