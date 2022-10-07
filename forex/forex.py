import fmpsdk
import toml
import datetime
import pandas as pd
from datetime import date 
from pprint import pprint
from func_forex import *
from func_cointegration import get_cointegrated_pairs
from func_excel import saveDFasExcel


import time
import json

def run():
    config = toml.load("./forex/forex.toml")
    apikey = config['apikey']
    forexPairs = config['forexPairs']
    timeFrame = config['timeFrame']
    historyFilename = "./forex/1_forex_price_history.json"
    excelFilename = "./forex/2_coint_pairs"
    sheetName = 'Forex'
    
    
    """
    # 1. Get price data
    priceHistoryDict = {}
    
    for forexPair in forexPairs:
        priceHistory = fmpsdk.historical_chart(apikey, forexPair, timeFrame)        
        
        if len(priceHistory) > 0: # type: ignore
            priceHistoryDict[forexPair] = priceHistory
            
    # Output prices to JSON
    if len(priceHistoryDict) > 0:
        with open(historyFilename, "w") as fp:
            json.dump(priceHistoryDict, fp, indent=4)
        print("Prices saved successfully.")
    
    """
    
    # 2. Calculate cointegration
    
    df = pd.DataFrame()
    
    print("Calculating co-integration...")
    with open(historyFilename) as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            price_data = cutForexPrices(price_data)
            df = get_cointegrated_pairs(price_data)

    saveDFasExcel(df, excelFilename, sheetName)


if __name__ == "__main__":
    run()