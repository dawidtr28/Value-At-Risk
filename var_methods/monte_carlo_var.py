import numpy as np

def monte_carlo_var(returns, confidence_level=0.05):
    mc_var = np.percentile(returns, confidence_level*100)
    mc_es = returns[returns <= mc_var].mean()
    return mc_var, mc_es