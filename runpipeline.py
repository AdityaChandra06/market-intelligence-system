import subprocess

PIPELINE_STEPS = [

    "python src/data/downloader.py",

    "python src/data/cleaner.py",

    "python src/features/technicals.py",

    "python src/regimes/labeler.py",

    "python src/volatility/targets.py",

    "python src/volatility/enrich_volatility_dataset.py",

    "python src/models/dataset_builder.py"
]


for step in PIPELINE_STEPS:

    print("\n" + "=" * 60)
    print(f"RUNNING: {step}")
    print("=" * 60)

    result = subprocess.run(step, shell=True)

    if result.returncode != 0:

        print(f"\nPipeline failed at: {step}")

        break

print("\nPipeline execution complete.")