# load_to_postgres.py
import psycopg2
import pandas as pd
import DateTime as dt
import os



# Read CSV file
csv_path = "/Users/adidas13/Downloads/My_python/data_master.csv"
df = pd.read_csv(csv_path)
log_file = "/Users/adidas13/Downloads/My_python/collect_log.txt"

print("✅ CSV loaded successfully — total rows:", len(df))
print(df.head())  # sanity check

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="sales_data",
    user="postgres",
    password="Meowmeow2025*",   
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert the data into the sales table
insert_query = """
INSERT INTO sales (salesdate, productid, region, freeship, discount, itemssold)
VALUES (%s, %s, %s, %s, %s, %s)
"""

rows_inserted = 0
for _, row in df.iterrows():
    cur.execute(insert_query, (
        row["salesdate"],
        row["productid"],
        row["region"],
        bool(row["freeship"]),
        row["discount"],
        row["itemssold"]
    ))
    rows_inserted += 1

print(f"✅ Inserted {rows_inserted} rows into sales table")

# Commit and close connection
conn.commit()
cur.close()
conn.close()

print("🎉 Done — Data successfully committed to PostgreSQL!")

with open(log_file, "a") as f:
    f.write(f"[{dt.datetime.now()}] Uploaded data to PostgreSQL successfully\n")