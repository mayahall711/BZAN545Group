from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask('project_folder_1')

# Fetch and summarize data
url = 'http://ballings.co/data.py'
exec(requests.get(url).content)  # creates 'data'
df = pd.DataFrame(data)
data = df.mean(numeric_only=True).to_dict()

@app.route("/summary")
def serve_data():
    return jsonify(data)

