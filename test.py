import yfinance as yf

ticker = 'AAPL'
period = '7d'
interval = '15m'

data = yf.download(ticker, period=period, interval=interval)
print(data)
