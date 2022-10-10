import fmpsdk
import toml
import datetime
import pandas as pd
from datetime import date 
from pprint import pprint
import time
import json

def run():
    config = toml.load("./forex/forex.toml")
    apikey = config['apikey']
    forexPairs = config['forexPairs']
    timeFrame = config['timeFrame']
    #timeStamp = time.strftime("%Y%m%d-%H%M%S")
    historyFilename = f"./forex/1_forex_price_history.json"
    
    # 1. Get price data
    
    print("Get price data from FMP...")
    
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


if __name__ == "__main__":
    run()