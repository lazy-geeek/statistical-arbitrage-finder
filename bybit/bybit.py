
import pandas as pd

from func_get_bybit_symbols import get_bybit_tradable_symbols
from func_prices_json import store_price_history

def run():
    
    # Get list of symbols
    
    sym_response = get_bybit_tradable_symbols()
    
    # Construct and save price history
    
    if len(sym_response) > 0:
        store_price_history(sym_response)


if __name__ == "__main__":
    run()