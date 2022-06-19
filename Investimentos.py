import pandas as pd
from pandas_datareader import data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()

ibov = web.get_data_yahoo('^BVSP', start='2021-05-03', end='2022-06-18')
print(ibov.head())
print(ibov.tail())
ibov["Close"].plot(figsize=(22,8), label="IBOV")
ibov["Close"].rolling(21).mean().plot(label="MM21")
ibov["Close"].rolling(200).mean().plot(label="MM200")
plt.legend()
plt.show()

ibov_fatiado = ibov[ibov.index.year == 2022]
ibov_fatiado["Close"].plot(figsize=(22,8), label="IBOV")
ibov_fatiado["Close"].rolling(21).mean().plot(label="MM21")
ibov_fatiado["Close"].rolling(200).mean().plot(label="MM200")
plt.legend()
plt.show()