import pandas as pd

df = pd.read_parquet("data/regimes/SPY.parquet")

print(df["regime"].value_counts())

print(df[[
    "close",
    "rolling_vol_20",
    "drawdown",
    "regime"
]].tail())