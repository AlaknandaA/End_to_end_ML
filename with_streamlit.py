import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import datetime


def save_stock_code():
    st.session_state['stock_code'] = st.session_state['stock_code']
    st.session_state['stock_details'] = yf.Ticker(str(st.session_state['stock_code']))

def from_date():
    st.session_state['from_date'] = st.session_state['from_date']
def to_date():
    st.session_state['to_date'] = st.session_state['to_date']
def stock_price_button():
    st.session_state['stock_price_button'] = False
def indicator_button():
    st.session_state['indicator_button'] = False


with st.sidebar:
    textbox = st.text_input("Input stock code", key='stock_code', on_change=save_stock_code)
    col1, col2 = st.columns([2, 2])
    with col1:
        date_picker1 = st.date_input(label='Pick from date',value=(datetime.date.today() - datetime.timedelta(90)), key='from_date', on_change=from_date)
    with col2:
        date_picker2 = st.date_input(label='Pick to date', key='to_date', on_change=to_date)
    col11, col22 = st.columns([5, 5])
    with col11:
        stock_price = st.button('Stock Price', on_click=stock_price_button)
    with col22:
        indicators = st.button('Indicators', on_click=indicator_button)
    no_of_days = st.number_input('enter no of days')
    forecast = st.button('Forecast')


if ('stock_code' in st.session_state) and ('stock_details' in st.session_state):
    try:
        stock_details = st.session_state['stock_details']
        st.image(stock_details.info['logo_url'])
        st.title(stock_details.info['shortName'])
        st.markdown(stock_details.info['longBusinessSummary'])
    except:
        st.title('Please enter a valid stock code')
else:
    st.title('Please enter a valid stock code')


if stock_price and ('stock_code' in st.session_state):
    aapl = yf.download(st.session_state['stock_code'],
                       start=st.session_state['from_date'],
                       end=st.session_state['to_date'],
                       progress=False)
    aapl = aapl.reset_index()
    fig = go.Figure(data=[go.Candlestick(
        x=aapl['Date'],
        open=aapl['Open'],
        close=aapl['Close'],
        high=aapl['High'],
        low=aapl['Low'])])
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")


if indicators and ('stock_code' in st.session_state):
    aapl = yf.download(st.session_state['stock_code'],
                       start=st.session_state['from_date'],
                       end=st.session_state['to_date'],
                       progress=False)
    aapl = aapl.reset_index()
    aapl['EWA_20'] = aapl['Close'].ewm(span=20, adjust=False).mean()
    fig = px.scatter(x=aapl['Date'],
                     y=aapl['EWA_20'],
                     title='Exponential Moving Average')
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
