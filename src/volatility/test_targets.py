import pandas as pd

df = pd.read_parquet("data/volatility/SPY.parquet")

print(df[[
    "rolling_vol_20",
    "future_vol_5d",
    "future_vol_10d",
    "vol_expansion"
]].tail())