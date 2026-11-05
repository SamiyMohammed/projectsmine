CREATE TABLE IF NOT EXISTS marts.fct_orders AS
SELECT
    o.order_id,
    o.customer_id,
    c.customer_state,
    o.order_status,
    o.order_purchase_ts,
    o.order_delivered_ts,
    o.order_estimated_delivery_ts,
    COALESCE(p.total_payment, 0) AS total_payment,
    DATE_PART('day', o.order_delivered_ts - o.order_purchase_ts) AS delivery_days
FROM staging.orders o
LEFT JOIN staging.customers c ON o.customer_id = c.customer_id
LEFT JOIN (
    SELECT order_id, SUM(payment_value) AS total_payment
    FROM staging.order_payments
    GROUP BY order_id
) p ON o.order_id = p.order_id;