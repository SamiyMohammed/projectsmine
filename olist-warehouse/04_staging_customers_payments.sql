CREATE TABLE IF NOT EXISTS staging.customers AS
SELECT
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix::int AS zip_code_prefix,
    customer_city,
    customer_state
FROM raw.customers
WHERE customer_id IS NOT NULL;

CREATE TABLE IF NOT EXISTS staging.order_payments AS
SELECT
    order_id,
    payment_sequential::int AS payment_sequential,
    payment_type,
    payment_installments::int AS payment_installments,
    payment_value::numeric(10,2) AS payment_value
FROM raw.order_payments
WHERE order_id IS NOT NULL;