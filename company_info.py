import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from yahoofinancials import YahooFinancials
import urllib
import os
import requests
from io import BytesIO
import tkinter as tk
import datetime


# today = datetime.date.today()
# today_minus_60 = datetime.date.today() - datetime.timedelta(60)
# print(today, today_minus_60)

# aapl = yf.download(tickers='AAPL')#,
#                     # start=today_minus_60,
#                     # end=today,
#                     # progress=False)
# print(aapl.head())
# aapl.reset_index(inplace=True)
# aapl.to_csv(r'C:\Users\user\Desktop\Jupyter_Files\End_to_end_ML\aapl.csv', index=False)


stock_info = yf.Ticker('AAPL')
print(stock_info, type(stock_info))
print(stock_info.info['logo_url'])