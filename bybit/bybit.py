import pandas as pd
import json

from func_get_bybit_symbols import get_bybit_tradable_symbols
from func_prices_json import store_price_history
from func_cointegration import get_cointegrated_pairs
from func_excel import saveDFasExcel

excelFilename = "./bybit/2_coint_pairs"
sheetName = 'Bybit'

def run():
    
    # Get list of symbols
    
    sym_response = get_bybit_tradable_symbols()
    
    # Construct and save price history
    
    if len(sym_response) > 0:
        store_price_history(sym_response)
    
    print("Calculating co-integration...")
    with open("./bybit/1_price_list.json") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            df = coint_pairs = get_cointegrated_pairs(price_data)
            saveDFasExcel(df, excelFilename, sheetName)
            print("Cointegration calculated !")

if __name__ == "__main__":
    run()