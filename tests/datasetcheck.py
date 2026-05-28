import pandas as pd

df = pd.read_parquet("data/regimes/SPY.parquet")
df2= pd.read_parquet("data/volatility/SPY.parquet")

print(df.columns)
print(df2.columns)