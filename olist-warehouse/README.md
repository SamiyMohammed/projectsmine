# Olist E-commerce Analytics Warehouse

A data pipeline that loads Brazilian e-commerce data into PostgreSQL, cleans it in layers, runs quality checks, and serves a dashboard in Metabase.

## Tech Stack
- PostgreSQL 16 in Docker
- Python (psycopg) for loading raw data
- SQL for staging, quality checks, and marts
- Metabase for dashboards

## Architecture
CSV files → `raw` schema → `staging` schema → `marts` schema → Metabase dashboard

- **raw:** data loaded as-is, all text columns
- **staging:** cleaned and typed (timestamps, numbers), invalid rows removed
- **marts:** `fct_orders`, one row per order, with payments and delivery time

## Dataset
Olist Brazilian E-Commerce Public Dataset on Kaggle. Download it and place these files in `data/raw/`:
- olist_orders_dataset.csv
- olist_customers_dataset.csv
- olist_order_payments_dataset.csv

## How to Run
1. Install Docker Desktop and make sure it's running.
2. Start the database and dashboard: `docker compose up -d`
3. Create the schemas and raw tables:
   - `docker exec -i olist_db psql -U analyst -d olist < 01_schemas.sql`
   - `docker exec -i olist_db psql -U analyst -d olist < 02_raw_tables.sql`
4. Install Python dependencies: `pip install "psycopg[binary]"`
5. Load the raw data: `python load_raw.py`
6. Build staging, checks, and marts, in order:
   - `03_staging_orders.sql`
   - `04_staging_customers_payments.sql`
   - `05_quality_checks.sql`
   - `06_marts.sql`
7. Open Metabase at http://localhost:3000 and connect it to the `olist` database (host `host.docker.internal`, port 5432, user and password `analyst`).

## Key Findings
- Monthly order volume and revenue grew steadily through 2017 and peaked in early 2018.
- Average delivery time is about 12 days.
- Total revenue across the dataset is about R$16.0 million.
- The sharp drop at the end of 2018 reflects sparse data at the edge of the dataset, not a real sales collapse.

## Notes
The database password is for local development only.
