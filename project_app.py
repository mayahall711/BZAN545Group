from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import datetime as dt
import requests

app = Dash(name='project_folder_1')

def serve_layout():
    response = requests.get("http://127.0.0.1:5000/")
    data = response.json()
    df = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])
    
    fig = px.bar(df, x="Metric", y="Value")
    
    return html.Div(children=[
        html.H1(children='Dynamic Dash App'),
        html.Div(children='This data is retrieved at ' + str(dt.datetime.now())),
        dcc.Graph(figure=fig)
    ])

app.layout = serve_layout
app.run(debug=True)
