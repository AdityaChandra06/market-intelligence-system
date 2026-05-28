import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_parquet(
    "data/volatility/SPY.parquet"
)

# Select numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Correlation matrix
corr = numeric_df.corr()

# Print correlations with target
print("\nCorrelation With Future Volatility:\n")

target_corr = corr["future_vol_5d"] \
    .sort_values(ascending=False)

print(target_corr)

# Plot heatmap
plt.figure(figsize=(12, 8))

plt.imshow(corr, aspect="auto")

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Feature Correlation Matrix")

plt.tight_layout()

plt.show()