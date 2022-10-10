import pandas as pd
from pprint import pprint
from func_forex import *
from func_cointegration import get_cointegrated_pairs
from func_excel import saveDFasExcel


import time
import json

def run():
    historyFilename = "./forex/1_forex_price_history.json"
    excelFilename = "./forex/2_coint_pairs"
    sheetName = 'Forex'    
    
    # 2. Calculate cointegration
    
    df = pd.DataFrame()
    
    print("Calculating co-integration...")
    with open(historyFilename) as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            price_data = cutForexPrices(price_data)
            df = get_cointegrated_pairs(price_data)

    saveDFasExcel(df, excelFilename, sheetName)
    print('Calculation complete !')


if __name__ == "__main__":
    run()