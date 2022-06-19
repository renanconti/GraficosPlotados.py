import pandas as pd
from pandas_datareader import data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
yf.pdr_override()

# ibov = web.get_data_yahoo('^BVSP', start='2021-05-03', end='2022-06-18')
# dolar = web.get_data_yahoo('USDBRL=X', start='2000-05-05', end='2022-06-18')
# print(ibov.head())
# print(ibov.tail())
# ibov["Close"].plot(figsize=(22,8), label="IBOV")
# ibov["Close"].rolling(21).mean().plot(label="MM21")
# ibov["Close"].rolling(200).mean().plot(label="MM200")
# plt.legend()
# plt.show()
#
# ibov_fatiado = ibov[ibov.index.year == 2022]
# ibov_fatiado["Close"].plot(figsize=(22,8), label="IBOV")
# ibov_fatiado["Close"].rolling(21).mean().plot(label="MM21")
# ibov_fatiado["Close"].rolling(200).mean().plot(label="MM200")
# plt.legend()
# plt.show()

# # dolar = dolar[dolar.index.year == 2022]
# dolar ["Close"].plot(figsize=(22,8), label="Dolar")
# dolar ["Close"].rolling(21).mean().plot(label='MM21', color='grey')
# dolar ["Close"].rolling(9).mean().plot(label='MM9', color='yellow')
# dolar ["Close"].rolling(50).mean().plot(label='MM50', color='red')
# dolar ["Close"].rolling(200).mean().plot(label='MM200')
# plt.legend()
# plt.show()

tickers = ['^BVSP', 'USDBRL=X', 'VALE3.SA', 'PETR4.SA']
carteira = web.get_data_yahoo(tickers, start='2010-01-01', end='2022-06-19')['Close']
carteira = carteira.dropna()
sns.set()
carteira.plot(subplots=True, figsize=(22,8))
carteira.columns = ['Petrobras', 'Dolar', 'Vale', 'Ibov']
# print(carteira)
plt.legend()
plt.show()

# sns.heatmap(carteira.corr(), annot=True)
# plt.show()
