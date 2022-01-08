import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Welcome to the stocks dash app!'),
    html.Div([
        html.P('This is my first dash webapp', style={'color':'blue', 'font_size':39}),
        html.P('what does it look like?'),
        html.P('I am rather proud of it'),
        html.Button('Stock Price', id='stock_price_button', n_clicks=1),
        html.Button('Indiators', id='indicators', n_clicks=1),
        html.Button('no. of days of forecast input', id='no_of_days', n_clicks=1),
        html.Button('forecast', id='forecast', n_clicks=1)
    ]),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)