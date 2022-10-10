from func_forex import *
from func_plot import plot_trends

import json

def run():
    historyFilename = "./forex/1_forex_price_history.json"
    
    sym_1 = 'CADCHF'
    sym_2 = 'NZDCHF'
        
    # 3. Plot cointegrated charts    
    
    print(f"Plotting data for {sym_1} {sym_2}...")
    with open(historyFilename) as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            price_data = cutForexPrices(price_data)
            plot_trends(sym_1, sym_2, price_data)
            
if __name__ == "__main__":
    run()