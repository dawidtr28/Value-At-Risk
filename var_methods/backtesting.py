import numpy as np
import scipy.stats as st

def kupiec_test(returns, var, alpha=0.05):
    T = len(returns)
    x = np.sum(returns < var)
    pi = x/T

    log0 = x * np.log(alpha) + (T - x) * np.log(1 - alpha)
    log1 = x * np.log(pi) + (T - x) * np.log(1 - pi) if 0 < pi < 1 else -np.inf

    LR = -2 * (log0 - log1)
    p_value = 1 - st.chi2.cdf(LR, df=1)

    print(f'Number of violations: {x}')
    print(f'Kupiec\'s Statistic (LR): {LR:.4f}')
    print(f'p-value: {p_value:.4f}')