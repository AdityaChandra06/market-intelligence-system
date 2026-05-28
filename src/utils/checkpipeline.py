from pathlib import Path

required_dirs = [
    "data/raw",
    "data/processed",
    "data/features",
    "data/regimes",
    "data/volatility",
    "data/datasets"
]

for directory in required_dirs:

    path = Path(directory)

    if path.exists():

        print(f"[OK] {directory}")

    else:

        print(f"[MISSING] {directory}")