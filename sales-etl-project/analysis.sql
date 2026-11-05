-- Sales Analysis Queries
-- Database: data/sales.db (table: sales)

-- Q1: Which products generate the most revenue?
SELECT product,
       COUNT(*) AS orders,
       ROUND(SUM(total_sales), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- Q2: What is the monthly revenue trend?
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(total_sales), 2) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Q3: Which sales reps have the highest average order value?
SELECT sales_rep,
       ROUND(AVG(total_sales), 2) AS avg_order_value
FROM sales
GROUP BY sales_rep
ORDER BY avg_order_value DESC;