import scipy.stats as st

def parametric_var(returns, confidence_level=0.05):
    df, loc, scale = st.t.fit(returns)
    p_var = st.t.ppf(confidence_level, df=df, loc=loc, scale=scale)
    p_es = returns[returns <= p_var].mean()
    return p_var, p_es, df, loc, scale