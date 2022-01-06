# End_to_end_ML
my first end to end ML project with Muskaan

[@Project reference](https://www.crio.do/projects/python-forecasting-stocks-dash/)

Let's do it!

Topics to be covered:
- Dash python
- Regression based ML
- Real-time data fetching: `yfinance` 
- Python visualizations: `plotly` 
- Stock market analysis 
- Deployment: Heroku
- Web dev: HTML & CSS

Project context:
- Stock investments provide one of the highest returns in the market. Even though they are volatile in nature, one can visualise share prices and other statistical factors which helps the keen investors carefully decide on which company they want to spend their earnings on.
- Developing this project idea using the Dash library (of Python), we can make dynamic plots of the financial data of a specific company by using the tabular data provided by yfinance python library. On top of it we can use a machine learning algorithm to predict the upcoming stock prices.


File structure is as follows:
- `app.py` contains web layout and server function. We will be referring to it as our main file.
- `model.py` is where we will implement a machine learning model for forecasting the stock price.
- The `assets` folder is where we keep our CSS files for styling and any other miscellaneous files like images (if u wish to include it in your site)
- `requirements.txt` is created so that other developers can install the correct versions of the required Python packages to run your Python code.
- The `Procfile` is created for deployment using Heroku. It is not needed to run the app locally.

Note:
- `numpy` library is used for multi-dimensional array operations.
- `pandas` is used for creating DataFrames to efficiently manage the data.
- `yfinance` is a library that allows us to fetch financial data of a company (since its listing in the stock market) from its stock code directly.
- `gunicorn` and `lxml` libraries will be used for the application's deployment i.e. to host the app on a target server.
- `sklearn` and `scikit-learn` are tools used in the development of Machine Learning (ML) models.