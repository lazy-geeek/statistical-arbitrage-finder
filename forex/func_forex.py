from pprint import pprint

def cutForexPrices(price_data):

    # Cut price history to 864 records -> 3 days of 5min timeframe
    
    for pair in price_data.keys():
        price_data[pair] = price_data[pair][0:864]
        
    return price_data   
    
