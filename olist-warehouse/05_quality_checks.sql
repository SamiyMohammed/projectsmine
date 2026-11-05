SELECT 'orders_duplicate_ids' AS check_name, COUNT(*) AS problem_rows
FROM (SELECT order_id FROM staging.orders GROUP BY order_id HAVING COUNT(*) > 1) d;

SELECT 'orders_missing_customer' AS check_name, COUNT(*) AS problem_rows
FROM staging.orders o
LEFT JOIN staging.customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

SELECT 'negative_payments' AS check_name, COUNT(*) AS problem_rows
FROM staging.order_payments
WHERE payment_value < 0;


SELECT 'bad_purchase_dates' AS check_name, COUNT(*) AS problem_rows
FROM staging.orders
WHERE order_purchase_ts < '2016-01-01' OR order_purchase_ts > now();