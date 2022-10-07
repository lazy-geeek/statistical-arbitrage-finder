from statsmodels.tsa.stattools import coint
import statsmodels.api as sm
import pandas as pd
import numpy as np
import math

def get_cointegrated_pairs(prices):
    
    # Loop through coins and check for co-integration
    coint_pair_list = []
    included_list = []
    
    count = 0
    
    for sym_1 in prices.keys():

        # Check each coin against the first (sym_1)
        for sym_2 in prices.keys():
            if sym_2 != sym_1:
                
                # Get unique combination id and ensure one off check
                sorted_characters = sorted(sym_1 + sym_2)
                unique = "".join(sorted_characters)
                #print(unique)
                count += 1 
                if unique in included_list:
                    continue
                
                # Get close prices
                series_1 = extract_close_prices(prices[sym_1])
                series_2 = extract_close_prices(prices[sym_2])

                # Check for cointegration and add cointegrated pair
                coint_flag, p_value, t_value, c_value, hedge_ratio, zero_crossings = calculate_cointegration(series_1, series_2)

                included_list.append(unique)
                coint_pair_list.append({
                    "sym_1": sym_1,
                    "sym_2": sym_2,
                    "coint": coint_flag,
                    "p_value": p_value,
                    "t_value": t_value,
                    "c_value": c_value,
                    "hedge_ratio": hedge_ratio,
                    "zero_crossings": zero_crossings
                })

    # Output results
    df_coint = pd.DataFrame(coint_pair_list)
    df_coint = df_coint.sort_values("zero_crossings", ascending=False)    
    return df_coint


# Put close prices into a list
def extract_close_prices(prices):
    close_prices = []
    for price_values in prices:
        if math.isnan(price_values["close"]):            
            return[]
        close_prices.append(price_values["close"])
    return close_prices


# Calculate co-integration
def calculate_cointegration(series_1, series_2):
    coint_flag = 0
    coint_res = coint(series_1, series_2)
    coint_t = coint_res[0]
    p_value = coint_res[1]
    critical_value = coint_res[2][1]
    model = sm.OLS(series_1, series_2).fit()
    hedge_ratio = model.params[0]
    spread = calculate_spread(series_1, series_2, hedge_ratio)
    zero_crossings = len(np.where(np.diff(np.sign(spread)))[0])
    if p_value < 0.5 and coint_t < critical_value:
        coint_flag = 1
    return (coint_flag, p_value, round(coint_t, 2), round(critical_value, 2), round(hedge_ratio, 2), zero_crossings)

# Calculate spread
def calculate_spread(series_1, series_2, hedge_ratio):
    spread = pd.Series(series_1) - (pd.Series(series_2) * hedge_ratio)
    return spread