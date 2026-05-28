from src.data.loader import load_asset

df = load_asset("SPY")

print(df.head())
print(df.info())