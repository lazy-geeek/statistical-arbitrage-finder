from func_cointegration import extract_close_prices, calculate_cointegration, calculate_spread, calculate_zscore
from func_excel import saveDFasExcel
import pandas as pd
import numpy as np
from pprint import pprint

excelFilename = "./forex/3_backtest_data"
sheetName = 'Backtest'    

# Plot prices and trends
def generate_backtest_data(sym_1, sym_2, price_data):

    # Extract prices
    prices_1 = extract_close_prices(price_data[sym_1])
    prices_2 = extract_close_prices(price_data[sym_2])

    # Get spread and zscore
    coint_flag, p_value, t_value, c_value, hedge_ratio, zero_crossing = calculate_cointegration(prices_1, prices_2)
    spread = calculate_spread(prices_1, prices_2, hedge_ratio)
    zscore = calculate_zscore(spread)

    # Calculate percentage changes
    df = pd.DataFrame(columns=[sym_1, sym_2])
    df[sym_1] = prices_1
    df[sym_2] = prices_2
    df[f"{sym_1}_pct"] = df[sym_1] / prices_1[0]
    df[f"{sym_2}_pct"] = df[sym_2] / prices_2[0]
    series_1 = df[f"{sym_1}_pct"].astype(float).values
    series_2 = df[f"{sym_2}_pct"].astype(float).values
    
    # Save results 
    df_2 = pd.DataFrame()
    df_2[sym_1] = prices_1
    df_2[sym_2] = prices_2
    df_2["Spread"] = spread
    df_2["zscore"] = zscore       
    
    # Delete rows with zscore = NaN
    
    df_2.dropna(inplace=True)    
    
    saveDFasExcel(df_2, excelFilename, sheetName)
    print('Backtesting data created !')    
