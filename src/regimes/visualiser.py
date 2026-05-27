import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

df= pd.read_parquet(Path("data/regimes/XOM.parquet"))

# Create a color mapping for regimes
regime_colors = {
    "sideways": "blue",
    "bear": "orange",
    "panic": "red",
    "bull": "green"
}

#Creating a figure

fig=go.Figure()

# Price line
fig.add_trace(
    go.Scatter(
        x=df.index,
        y=df["close"],
        mode="lines",
        name="XOM Close",
        line=dict(color="blue")
    )
)

# Add regime markers
for regime, color in regime_colors.items():

    regime_df = df[df["regime"] == regime]

    fig.add_trace(
        go.Scatter(
            x=regime_df.index,
            y=regime_df["close"],
            mode="markers",
            name=regime,
            marker=dict(
                color=color,
                size=4
            )
        )
    )

# Layout
fig.update_layout(
    title="XOM Market Regimes",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_dark",
    height=700
)

# Show chart
fig.show()


vol_fig = go.Figure()

vol_fig.add_trace(
    go.Scatter(
        x=df.index,
        y=df["rolling_vol_20"],
        mode="lines",
        name="20-Day Volatility"
    )
)

vol_fig.update_layout(
    title="XOM Rolling Volatility",
    xaxis_title="Date",
    yaxis_title="Volatility",
    template="plotly_dark",
    height=500
)

vol_fig.show()