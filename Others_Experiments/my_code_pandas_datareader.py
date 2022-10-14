# %%====
from pandas_datareader.data import DataReader  # conda install pandas-datareader

data = DataReader(['AAPL', 'AMZN', 'GOOG', 'MFST'], 'yahoo', start='2015-01-01', end='2021-08-30')
print(data)

# %%=====================
import yfinance as yf

etf = ['AXP', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'XOM', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'KO']  # and any tickers you'd add to be retrived
tit = yf.download(tickers=etf, period='max')

