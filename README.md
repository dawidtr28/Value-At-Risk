# Value-At-Risk
Portfolio Value at Risk (VaR) Calculator – Python project for calculating and visualizing portfolio risk using multiple VaR methods (Historical, Parametric, Monte Carlo) with plotting and backtesting.

## Overview
This project provides multiple methods for calculating **Value at Risk (VaR)** and **Expected Shortfall (CVaR)** for a portfolio of assets, using Python.  
It includes:
- Historical Simulation
- Parametric VaR (t-distribution fitting)
- Monte Carlo Simulation
- Backtesting (Kupiec's Test, Christoffersen's Test)
  
The project is designed to be **user-friendly**, with all key inputs defined in a single configuration file and a simple runner script to execute selected methods.

## Repository Structure
```
var_project/
│
├── project_runner/
│ ├── input_config.py # User-defined inputs and method selection
│ ├── run_examples.py # Main script to run VaR calculations
│
├── var_methods/
│ ├── data_preparation.py # Fetching data and calculating returns
│ ├── historical_var.py # Historical Simulation VaR
│ ├── parametric_var.py # Parametric (t-distribution) VaR
│ ├── monte_carlo_var.py # Monte Carlo Simulation VaR
│ ├── backtesting.py # Kupiec Test for VaR backtesting
│
├── LICENSE # MIT License
├── README.md # Project documentation
├── requirements.txt # Required Python packages
└── .gitignore # Ignored files for Git
```

## Usage
1. Open project_runner/input_config.py and adjust:
```python
tickers = ['EXUS.DE', 'CNDX.L', 'EIMI.L', 'IGLN.L'] #(use Yahoo Finance website for tickers)
weights = np.array([0.3, 0.3, 0.3, 0.1])
period = '2y'
conf_level = 0.05
num_simulations = 100000

run_historical = True
run_parametric = True
run_monte_carlo = True
```

2. Run Analysis
python project_runner/run_examples.py

```
The script will:
    - Fetch data
    - Calculate returns
    - Run selected VaR methods
    - Display results and plots
    - Perform backtesting (Kupiec Test)
```

## License
This project is licensed under the MIT License

## Requirements
See requirements.txt for dependencies:
```
numpy
scipy
matplotlib
yfinance
```
