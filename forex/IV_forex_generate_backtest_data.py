from func_forex import *
from func_backtest import generate_backtest_data

import json

def run():
    historyFilename = "./forex/1_forex_price_history.json"
    
    sym_1 = 'CADCHF'
    sym_2 = 'NZDCHF'
        
    # 4. Generate Backtest data    
    
    print(f"Generating backtesting data for {sym_1} {sym_2}...")
    with open(historyFilename) as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            price_data = cutForexPrices(price_data)
            generate_backtest_data(sym_1, sym_2, price_data)
            
if __name__ == "__main__":
    run()