from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import datetime as dt
import random

data = pd.read_csv("data_master.csv")

data.describe()
data.info()
data.groupby('region').itemssold.mean()

app = Dash(name = 'BAS 545')


def serve_layout():  
    fig = px.bar(data, x="region", y = "itemssold")

    return html.Div(children= [
    html.H1(children = 'Dynamic Dash App'), #H1 is a header
    html.Div(children = 'This data is retrieved at ' + str(dt.datetime.now())),
    dcc.Graph(
            id = 'example-graph',
            figure= fig
    )
])

app.layout = serve_layout

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)