DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL,
    customer_name TEXT,
    sale_date DATE
);
