"""
Step 1: Simulate messy sales data, clean it, and load it into SQLite.
"""
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

# ---------- Configuration ----------
RANDOM_SEED = 42          # Makes the "random" data identical every run
N_ROWS = 1000             # Number of simulated transactions
RAW_CSV = Path("data/raw_sales.csv")
DB_PATH = Path("data/sales.db")

rng = np.random.default_rng(RANDOM_SEED)


# ---------- 1. EXTRACT: simulate messy raw data ----------
def generate_raw_data(n_rows: int) -> pd.DataFrame:
    """Create a fake sales table with realistic problems baked in."""
    products = ["Laptop", "Monitor", "Keyboard", "Mouse", "Headset"]
    prices = {"Laptop": 899.99, "Monitor": 199.50, "Keyboard": 49.00,
              "Mouse": 25.00, "Headset": 89.99}
    regions = ["Northeast", "Southeast", "Midwest", "West"]
    reps = ["Alice Chen", "Bob Smith", "Carla Diaz", "Dev Patel"]

    # Random dates spread across 2025
    start = pd.Timestamp("2025-01-01")
    dates = start + pd.to_timedelta(rng.integers(0, 365, n_rows), unit="D")

    product_choices = rng.choice(products, n_rows)
    df = pd.DataFrame({
        "transaction_id": [f"T{i:05d}" for i in range(1, n_rows + 1)],
        "order_date": dates.strftime("%Y-%m-%d"),
        "customer_id": rng.integers(1000, 1200, n_rows),
        "product": product_choices,
        "quantity": rng.integers(1, 6, n_rows),
        "unit_price": [prices[p] for p in product_choices],
        "region": rng.choice(regions, n_rows),
        "sales_rep": rng.choice(reps, n_rows),
    })

    # Problem 1: inconsistent text (extra spaces and ALL CAPS) in ~15% of regions
    messy = rng.random(n_rows) < 0.15
    df.loc[messy, "region"] = df.loc[messy, "region"].str.upper() + " "

    # Problem 2: missing values scattered across columns
    for col, fraction in [("customer_id", 0.05), ("unit_price", 0.03), ("sales_rep", 0.04)]:
        df.loc[rng.random(n_rows) < fraction, col] = np.nan

    # Problem 3: duplicate rows (about 3% of the data gets copied)
    duplicates = df.sample(frac=0.03, random_state=RANDOM_SEED)
    df = pd.concat([df, duplicates], ignore_index=True)

    return df


# ---------- 2. TRANSFORM: clean the data ----------
def clean_data(raw: pd.DataFrame) -> pd.DataFrame:
    """Fix formatting, handle missing values, and remove duplicates."""
    print(f"Raw rows received:        {len(raw)}")
    print(f"Missing values per column:\n{raw.isna().sum()}\n")

    df = raw.copy()

    # Standardize text: remove extra spaces and fix capitalization
    df["region"] = df["region"].str.strip().str.title()

    # Missing sales rep -> label as "Unknown" (keeps the sale, flags the gap)
    df["sales_rep"] = df["sales_rep"].fillna("Unknown")

    # Missing price -> fill with the median price for that product
    df["unit_price"] = df["unit_price"].fillna(
        df.groupby("product")["unit_price"].transform("median")
    )

    # Missing customer ID -> we can't attribute the sale, so drop the row
    df = df.dropna(subset=["customer_id"])
    df["customer_id"] = df["customer_id"].astype(int)

    # Convert text dates into real date objects
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Remove duplicates: each transaction_id should appear exactly once
    df = df.drop_duplicates(subset="transaction_id")

    # Derived column for analysis
    df["total_sales"] = (df["quantity"] * df["unit_price"]).round(2)

    df = df.sort_values("order_date").reset_index(drop=True)

    print(f"Clean rows remaining:     {len(df)}")
    return df


# ---------- 3. LOAD: write to a local SQLite database ----------
def load_to_sqlite(df: pd.DataFrame, db_path: Path) -> None:
    """Save the cleaned DataFrame as a table called 'sales'."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        # if_exists="replace" overwrites the table, so re-running is safe
        df.to_sql("sales", conn, if_exists="replace", index=False)
    finally:
        conn.close()
    print(f"Loaded {len(df)} rows into '{db_path}' (table: sales)")


# ---------- 4. VERIFY: query the database to confirm it worked ----------
def verify_database(db_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    try:
        summary = pd.read_sql(
            """
            SELECT region,
                   COUNT(*)                   AS orders,
                   ROUND(SUM(total_sales), 2) AS revenue
            FROM sales
            GROUP BY region
            ORDER BY revenue DESC
            """,
            conn,
        )
        print("\nRevenue by region (queried from SQLite):")
        print(summary.to_string(index=False))
    finally:
        conn.close()


# ---------- Run the pipeline ----------
if __name__ == "__main__":
    raw_df = generate_raw_data(N_ROWS)
    RAW_CSV.parent.mkdir(parents=True, exist_ok=True)
    raw_df.to_csv(RAW_CSV, index=False)   # Keep the messy copy for reference

    clean_df = clean_data(raw_df)
    load_to_sqlite(clean_df, DB_PATH)
    verify_database(DB_PATH)

    pd.read_sql("SELECT * FROM sales", sqlite3.connect(DB_PATH)).to_csv("data/sales.csv", index=False)