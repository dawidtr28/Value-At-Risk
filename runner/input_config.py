import numpy as np

# ------------------------------- EDITABLE -------------------------------
tickers = ['AMZN', 'AAPL', 'MSFT', 'PFE']
weights = np.array([0.3, 0.3, 0.3, 0.1])
period = '2y'
conf_level = 0.05
num_simulations = 10000  # Only for Monte Carlo

run_historical = True
run_parametric = True
run_monte_carlo = True

# ------------------------------------------------------------------------

