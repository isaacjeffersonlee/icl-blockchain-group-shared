import yfinance as yf

msft = yf.Ticker("PAXG-USD")

"""
interval : str
    Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    Intraday data cannot extend last 60 days
"""
hist = msft.history(period="1mo", interval="1h")

print(hist)
