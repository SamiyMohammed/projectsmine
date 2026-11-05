CREATE TABLE IF NOT EXISTS raw.orders (
    order_id text,
    customer_id text,
    order_status text,
    order_purchase_timestamp text,
    order_approved_at text,
    order_delivered_carrier_date text,
    order_delivered_customer_date text,
    order_estimated_delivery_date text
);

CREATE TABLE IF NOT EXISTS raw.customers (
    customer_id text,
    customer_unique_id text,
    customer_zip_code_prefix text,
    customer_city text,
    customer_state text
);

CREATE TABLE IF NOT EXISTS raw.order_payments (
    order_id text,
    payment_sequential text,
    payment_type text,
    payment_installments text,
    payment_value text
);