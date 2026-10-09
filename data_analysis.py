"""Load, inspect, clean, summarize, and plot the sample dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    df = pd.read_csv(DATA_PATH)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    print("First five rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nNumeric summary:")
    print(df.describe(numeric_only=True))

    # Save a region-level summary.
    summary = df.groupby("region", as_index=False).agg(
        total_orders=("orders", "sum"),
        average_delivery_days=("delivery_days", "mean"),
        average_customer_rating=("customer_rating", "mean"),
    )
    summary.to_csv(OUTPUT_DIR / "region_summary.csv", index=False)
    print("\nRegion summary:")
    print(summary)

    correlation = df[["orders", "delivery_days", "customer_rating"]].corr()
    correlation.to_csv(OUTPUT_DIR / "correlation_matrix.csv")
    print("\nCorrelation matrix:")
    print(correlation)

    ax = df.groupby("region")["orders"].sum().sort_values().plot(kind="bar")
    ax.set_title("Total Orders by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Orders")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "orders_by_region.png", dpi=150)
    plt.close()
    print(f"\nOutputs saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
