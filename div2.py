from re import T
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

#flask setup
app = dash.Dash(__name__)
server = app.server

#web layout
app.layout = html.Div([item1, item2])

item2 = html.Div([
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

if __name__ == '__main__':
    app.run_server(debug=True)
