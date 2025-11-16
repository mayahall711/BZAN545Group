# api.py
import requests
from flask import Flask, jsonify
import pandas as pd

app = Flask('project_folder_1')

# Fetch data once
url = 'http://ballings.co/data.py'
exec(requests.get(url).content)  # creates 'data'

df = pd.DataFrame(data)

# Optional: precompute KPIs
summary = {
    'total_items_sold': int(df['itemssold'].sum()),
    'avg_discount': round(df['discount'].mean(), 2),
    'percent_free_shipping': round((df['freeship'].sum() / len(df)) * 100, 2)
}

@app.route("/")
def serve_data():
    return jsonify({
        'summary': summary,
        'data': df.to_dict(orient='records')  # all rows
    })

if __name__ == '__main__':
    app.run(debug=True)

# Use command prompt: python3 -m flask --app (copied path) run