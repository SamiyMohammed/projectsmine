CREATE TABLE IF NOT EXISTS staging.orders AS
SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp::timestamp AS order_purchase_ts,
    order_delivered_customer_date::timestamp AS order_delivered_ts,
    order_estimated_delivery_date::timestamp AS order_estimated_delivery_ts
FROM raw.orders
WHERE order_id IS NOT NULL;