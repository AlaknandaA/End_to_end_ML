from re import T
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import plotly.express as px
import pandas as pd

#flask setup
app = dash.Dash(__name__)
server = app.server

#web layout
# app.layout = html.Div([item1, item2])

app.layout = html.Div([
    html.Div([
        #logo
        #company name
    ], className="company_header"),

    html.Div(
        #company description
        id = "description",className = "description_ticker"),
    
    html.Div(
        [#Stock price plot
        ], id = "graphs-content"),
    
    html.Div([
        #indicators plot
    ], id = "main-content"),

    html.Div([
        #forecast-content
    ], id="forecast-content")
], className="stock_content")




#dash layout tutorial
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
