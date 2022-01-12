import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import date
# import dash_input_components as Input
# from dash import Dash, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P('Welcome to the stocks dash app!', className="container1",
           style={
               'color':'#00361c',
               'text-align':'left',
               'font-size':'25px'
           }),
    html.P('Please input stock code:', style={
        'margin-top':'50px',
        'font-size':'18px'
    }),
    html.Div(className="two columns",
             children=[
        dcc.Input(id='input-on-stockcode', type='text', className="container2",
                           style={
                               'display':'inline-block',
                               'backgroundColor':'lightblue',
                               'margin-top':'5px',
                               'height':'21.5px',
                               'margin-left': '5px',
                           }),
        html.Button('Submit', id='submit-stockcode', n_clicks=0, className="container3",
                    style={
                        'display':'inline-block',
                        'backgroundColor':'lightblue',
                        'margin-top':'5px',
                        'font-size':'18px',
                        'height':'27px'
                    })
    ]),
    html.Div(
        dcc.DatePickerRange(className="container3",
            id='my-date-picker-range',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 9),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25),
            display_format='Do MMM, YY'
        ), style={
            'margin-top':'50px',
            'margin-left': '5px',
        }
        ),
    html.Div(className = "container3",
             children=[
                 html.Button('Stock Price', id='stock_price_button', n_clicks=1,
                  style = {
                      'display': 'inline-block',
                      'backgroundColor': 'lightblue',
                      'margin-top': '50px',
                      'margin-left': '5px',
                      'height': '23px',
                      'font-size':'18px'
                  }
                             ),
                 html.Button('Indiators', id='indicators', n_clicks=1,
                             style={
                                 'display': 'inline-block',
                                 'backgroundColor': 'lightblue',
                                 'margin-top': '50px',
                                 'margin-left': '50px',
                                 'height': '23px',
                                 'font-size':'18px'
                             }
                             )
             ]),
    html.Div(className="container3",
             children=[
                 dcc.Input(id='no_of_days', type='text',style={
                               'display':'inline-block',
                               'backgroundColor':'lightblue',
                               'margin-top':'5px',
                               'height':'21.5px',
                     'margin-left': '5px',
                           }),
                 html.Button('forecast', id='forecast', n_clicks=1,style={
                               'display':'inline-block',
                               'backgroundColor':'lightblue',
                               'margin-top':'5px',
                               'height':'27px',
                     'font-size':'18px'
                           })
             ],style={
            'margin-top':'50px'
        })
    ],style={'backgroundColor':'lightslategray'})

"""
@app.callback(
    Output('output-container-date-picker-range', 'children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    return 'The start date is {} and the end date is {}'.format(
        start_date,
        end_date
    )
"""

if __name__ == '__main__':
    app.run_server(debug=True)