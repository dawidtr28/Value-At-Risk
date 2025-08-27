import numpy as np

def historical_var(returns, confidence_level=0.05):
    h_var = np.percentile(returns, confidence_level*100)
    h_es = returns[returns<= h_var].mean()
    return h_var, h_es