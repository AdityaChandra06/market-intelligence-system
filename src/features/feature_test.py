import pandas as pd

df = pd.read_parquet("data/features/SPY.parquet")

print(df.columns)

print(df.head())