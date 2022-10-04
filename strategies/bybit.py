
import pandas as pd

from func_get_bybit_symbols import get_bybit_tradable_symbols

def run():
    
    # Get list of symbols
    
    sym_response = get_bybit_tradable_symbols()
    


if __name__ == "__main__":
    run()