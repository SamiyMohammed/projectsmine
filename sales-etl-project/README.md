# Sales ETL Pipeline and Dashboard

An end-to-end project that generates messy sales transaction data, cleans it with Python and Pandas, loads it into a SQLite database, and visualizes the results in Power BI.

## Tools Used

- Python and Pandas for extraction, transformation, and loading
- SQLite for storage
- SQL for analysis
- Power BI Desktop for the dashboard

## How to Run

1. Install the required libraries: `pip install pandas numpy`
2. Run the pipeline: `python etl_pipeline.py`

This creates `data/sales.db` and `data/sales.csv`, and prints a data quality report showing how many rows were cleaned.

## Key Findings

- Laptops generate the most revenue by a wide margin, followed by monitors.
- Monthly revenue shows how sales change across 2025.
- The pipeline reduced 1,030 raw rows to 952 clean rows after removing duplicates and handling missing values.

## Files

- `etl_pipeline.py`: the ETL script
- `analysis.sql`: SQL queries for the sales analysis
- `sales-dashboard.pbix`: the Power BI dashboard
