import numpy as np
import yfinance as yf

def get_data(tickers, weights, period='2y'):
    prices = yf.download(tickers, period=period,)['Close']
    prices = prices.interpolate(method='linear')
    log_returns = np.log(prices / prices.shift(1)).dropna()
    portfolio_log_returns = log_returns.dot(weights)
    return prices, portfolio_log_returns