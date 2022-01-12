import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as date
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Welcome to the stocks dash app!'),
    html.Div(
        html.P('Input Stock Code'),
        html.Div(dcc.Input(id='input-stockcode', type='text')),
        html.Button('Submit', id='submit-stockcode', n_clicks=0),
        html.Div([
            html.Div(
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2022, 1, 9),
                    initial_visible_month=date(2017, 8, 5),
                    end_date=date(2017, 8, 25),
                    display_format='Do MMM, YY'
                )
                ),
            html.Div(id='output-container-date-picker-range')
        ]),
        html.Button('Stock Price', id='stock_price_button', n_clicks=1),
        html.Button('Indiators', id='indicators', n_clicks=1),
        html.Button('no. of days of forecast input', id='no_of_days', n_clicks=1),
        html.Button('forecast', id='forecast', n_clicks=1)
    )
])

# @app.callback(
#     # Output('container-button-basic', 'children'),
#     Input('submit-stockcode', 'n_clicks'),
#     State('input-stockcode', 'value')
# )


# app.layout = html.Div([
#     html.Div(dcc.Input(id='input-on-submit', type='text')),
#     html.Button('Submit', id='submit-val', n_clicks=0),
#     html.Div(id='container-button-basic',
#              children='Enter a value and press submit')
# ])


# @app.callback(
#     Output('container-button-basic', 'children'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value')
# )
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )

if __name__ == '__main__':
    app.run_server(debug=True)