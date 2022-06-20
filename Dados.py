import mplfinance as mpl
import yfinance as yf

ticker = yf.Ticker("VALE3.SA")
hist = ticker.history(period="max")

hlines = [80, 90]
vlines = ['2022-02-01', '2022-03-01', '2022-04-01']

mpl.plot(hist[-100:], type="candle", mav=20, hlines=hlines, vlines=vlines, volume=True)

