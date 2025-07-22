import pandas as pd
import sqlite3

# Step 1: Read the CSV file
df = pd.read_csv("data/sales_data.csv")

# Step 2: Add a new column - total_amount
df["total_amount"] = df["quantity"] * df["price"]

# Step 3: Connect to SQLite database
conn = sqlite3.connect("data_warehouse.db")
cursor = conn.cursor()

# Step 4: Load schema (drop & create table)
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Step 5: Insert data into 'sales' table
df[["sale_id", "product", "quantity", "price", "customer_name", "sale_date"]].to_sql(
    "sales", conn, if_exists="append", index=False
)

print("✅ Data loaded into the data warehouse (SQLite DB).")

conn.commit()
conn.close()
