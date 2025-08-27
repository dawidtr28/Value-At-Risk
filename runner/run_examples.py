import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

from var_methods.data_preparation import get_data
from var_methods.historical_var import historical_var
from var_methods.parametric_var import parametric_var
from var_methods.monte_carlo_var import monte_carlo_var
from var_methods.backtesting import kupiec_test
from input_config import tickers, weights, period, conf_level, num_simulations
from input_config import run_historical, run_parametric, run_monte_carlo


prices, portfolio_log_returns = get_data(tickers, weights, period)


if run_historical:
    h_var, h_es = historical_var(portfolio_log_returns, conf_level)

    print(f'Historical VaR {conf_level*100:.0f}% = {h_var*100:.2f}%')
    print(f'Historical Expected Shortfall (CVaR) {conf_level*100:.0f}% = {h_es*100:.2f}%')

    portfolio_log_returns.hist(bins=100, density=True)
    plt.axvline(h_var, color='red', linestyle='dashed', linewidth=1.5) 
    plt.text(h_var,
            plt.ylim()[1]*0.8,
            f'VaR {conf_level*100:.0f}% = {h_var:.4f}',
            color='red',
            rotation=90,
            va='center',
            ha='right')

    plt.axvline(h_es, color='darkviolet', linestyle='dashed', linewidth=1.5)
    plt.text(h_es,
            plt.ylim()[1]*0.8,
            f'CVaR {conf_level*100:.0f}% = {h_es:.4f}',
            color='darkviolet',
            rotation=90,
            va='center',
            ha='right')
    plt.show()

    kupiec_test(portfolio_log_returns, h_var)


if run_parametric:
    p_var, p_es, df, loc, scale = parametric_var(portfolio_log_returns, conf_level)
    
    print(f'Parametric VaR {conf_level*100:.0f}% = {p_var*100:.2f}%')
    print(f'Parametric Expected Shortfall (CVaR) {conf_level*100:.0f}% = {p_es*100:.2f}%')

    x = np.linspace(loc-7*scale, loc+7*scale) # x axis
    pdf = st.t.pdf(x, df=df, loc = loc, scale = scale) # probability density funcion
    plt.plot(x, pdf, color = 'red')
    plt.hist(portfolio_log_returns, density=True, bins = 100)
    plt.axvline(p_var, color='red', linestyle='dashed', linewidth=1.5)
    plt.text(p_var,
            plt.ylim()[1]*0.8, 
            f'VaR {conf_level*100:.0f}% = {p_var:.4f}',
            color='red',
            rotation = 90,
            va='center',
            ha='right')

    plt.axvline(p_es, color='darkviolet', linestyle='dashed', linewidth=1.5)
    plt.text(p_es,
            plt.ylim()[1]*0.8,
            f'CVaR {conf_level*100:.0f}% = {p_es:.4f}',
            color = 'darkviolet',
            rotation = 90,
            va = 'center',
            ha = 'right')
    plt.show()

    kupiec_test(portfolio_log_returns, p_var)


if run_monte_carlo:
    df, loc, scale = st.t.fit(portfolio_log_returns)
    random_log_returns = st.t.rvs(df=df, loc=loc, scale=scale, size = num_simulations)

    mc_var, mc_es = monte_carlo_var(random_log_returns, conf_level)

    print(f'Monte Carlo VaR {conf_level*100:.0f}% = {mc_var*100:.2f}%')
    print(f'Monte Carlo Expected Shortfall (CVaR) {conf_level*100:.0f}% = {mc_es*100:.2f}%')

    plt.hist(random_log_returns, density=True, bins = 100)
    plt.xlim(-0.07, 0.07)
    plt.axvline(mc_var, color='red', linestyle='dashed', linewidth=1.5)
    plt.text(mc_var,
            plt.ylim()[1]*0.8, 
            f'VaR {conf_level*100:.0f}% = {mc_var:.4f}',
            color='red',
            rotation = 90,
            va='center',
            ha='right')

    plt.axvline(mc_es, color='darkviolet', linestyle='dashed', linewidth=1.5)
    plt.text(mc_es,
            plt.ylim()[1]*0.8,
            f'CVaR {conf_level*100:.0f}% = {mc_es:.4f}',
            color = 'darkviolet',
            rotation = 90,
            va = 'center',
            ha = 'right')
    plt.show()

    kupiec_test(portfolio_log_returns, mc_var)

