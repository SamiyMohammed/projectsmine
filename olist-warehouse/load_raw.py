import psycopg

DSN = "postgresql://analyst:analyst@localhost:5432/olist"

# CSV filename -> target raw table
FILES = {
    "olist_orders_dataset.csv": "raw.orders",
    "olist_customers_dataset.csv": "raw.customers",
    "olist_order_payments_dataset.csv": "raw.order_payments",
}

def load_table(conn, csv_path, table):
    with conn.cursor() as cur:
        # Empty the table first so re-running doesn't duplicate rows
        cur.execute(f"TRUNCATE {table}")
        with open(csv_path, encoding="utf-8") as f:
            with cur.copy(f"COPY {table} FROM STDIN WITH (FORMAT csv, HEADER true)") as copy:
                while chunk := f.read(65536):
                    copy.write(chunk)
    print(f"Loaded {table}")

if __name__ == "__main__":
    with psycopg.connect(DSN) as conn:
        for filename, table in FILES.items():
            load_table(conn, f"data/raw/{filename}", table)
        conn.commit()