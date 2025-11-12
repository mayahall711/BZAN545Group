import datetime as dt
import requests
import pandas as pd
import os
import subprocess

# Where to save data and logs
data_file = "/Users/adidas13/Downloads/My_python/data_master.csv"
log_file = "/Users/adidas13/Downloads/My_python/collect_log.txt"

try:
    # Fetch the data from the URL
    url = "http://ballings.co/data.py"
    exec(requests.get(url).content)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # If the file exists → append without header
    if os.path.exists(data_file):
        df.to_csv(data_file, mode="a", header=False, index=False)
        msg = f"[{dt.datetime.now()}] Appended {len(df)} rows to {data_file}\n"
    else:
        df.to_csv(data_file, mode="w", header=True, index=False)
        msg = f"[{dt.datetime.now()}] Created {data_file} with {len(df)} rows\n"

    # Log success
    with open(log_file, "a") as f:
        f.write(msg)

except Exception as e:
    # Log failure
    with open(log_file, "a") as f:
        f.write(f"[{dt.datetime.now()}] ERROR: {str(e)}\n")

# Automatically load the updated CSV into PostgreSQL
try:
    subprocess.run([
        "python3",
        "/Users/adidas13/Downloads/My_python/load_sales_data.py"
    ])
    with open(log_file, "a") as f:
        f.write(f"[{dt.datetime.now()}] ✅ Data successfully loaded into PostgreSQL.\n")
except Exception as e:
    with open(log_file, "a") as f:
        f.write(f"[{dt.datetime.now()}] ❌ PostgreSQL load failed: {str(e)}\n")
