-- Total sales per product
SELECT product, SUM(quantity) AS total_units, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product;

-- Daily sales
SELECT sale_date, COUNT(*) AS num_sales, SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
