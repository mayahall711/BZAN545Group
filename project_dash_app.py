# dashboard.py
import requests
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Create Dash app
app = Dash(name='project_folder_1')

def serve_layout():
    # Fetch data from Flask API
    response = requests.get('http://127.0.0.1:5000/')  # Flask app must be running
    json_data = response.json()
    
    df = pd.DataFrame(json_data['data'])
    summary = json_data['summary']

    # Charts
    fig_product = px.bar(
        df.groupby('productid')['itemssold'].sum().reset_index(),
        x='productid', y='itemssold',
        title='Total Items Sold per Product'
    )

    fig_region = px.bar(
        df.groupby('region')['itemssold'].sum().reset_index(),
        x='region', y='itemssold',
        title='Total Items Sold per Region'
    )

    fig_discount = px.scatter(
        df, x='discount', y='itemssold', color='freeship',
        title='Discount vs Items Sold (Color = Free Shipping)',
        labels={'freeship': 'Free Shipping'}
    )

    heatmap_data = df.groupby(['region','productid'])['itemssold'].sum().reset_index()
    fig_heatmap = px.density_heatmap(
        heatmap_data, x='productid', y='region', z='itemssold',
        color_continuous_scale='Viridis',
        title='Heatmap of Items Sold by Product and Region'
    )

    return html.Div([
        html.H1("Sales Dashboard", style={'textAlign': 'center', 'marginBottom': 30}),

        # KPI cards
        html.Div([
            html.Div([html.H3("Total Items Sold"), html.H4(f"{summary['total_items_sold']}")],
                     style={'width':'30%','display':'inline-block','textAlign':'center'}),
            html.Div([html.H3("Average Discount"), html.H4(f"{summary['avg_discount']}")],
                     style={'width':'30%','display':'inline-block','textAlign':'center'}),
            html.Div([html.H3("% Free Shipping Orders"), html.H4(f"{summary['percent_free_shipping']}%")],
                     style={'width':'30%','display':'inline-block','textAlign':'center'}),
        ], style={'marginBottom':50}),

        # Charts
        html.Div([
            html.Div(dcc.Graph(figure=fig_product), style={'width':'48%','display':'inline-block'}),
            html.Div(dcc.Graph(figure=fig_region), style={'width':'48%','display':'inline-block'}),
        ]),
        html.Div([
            html.Div(dcc.Graph(figure=fig_discount), style={'width':'48%','display':'inline-block'}),
            html.Div(dcc.Graph(figure=fig_heatmap), style={'width':'48%','display':'inline-block'}),
        ])
    ])

app.layout = serve_layout

if __name__ == '__main__':
    app.run(debug=True)

