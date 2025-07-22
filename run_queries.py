import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("data_warehouse.db")
cursor = conn.cursor()

# Total sales per product
print("📦 Total sales per product:")
cursor.execute("""
SELECT product, SUM(quantity) AS total_units, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
""")
for row in cursor.fetchall():
    print(row)

# Daily revenue
print("\n📅 Daily revenue:")
cursor.execute("""
SELECT sale_date, COUNT(*) AS num_sales, SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date
""")
for row in cursor.fetchall():
    print(row)

conn.close()
