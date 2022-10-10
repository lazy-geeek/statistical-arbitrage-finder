from pprint import pprint
from bybit_config import session
from pprint import pprint

def get_bybit_tradable_symbols():
    sym_list = []
    symbols = session.query_symbol()
    tickers = session.latest_information_for_symbol()    
    tickers = tickers["result"]
    if "ret_msg" in symbols.keys():
        if symbols["ret_msg"] == "OK":
            symbols = symbols["result"]
            for symbol in symbols:                
                if symbol["quote_currency"] == "USDT" and symbol["status"] == "Trading":
                        for ticker in tickers:
                            if ticker["symbol"] == symbol["alias"]:
                                if ticker["volume_24h"] > 500000:
                                    sym_list.append(symbol)
            
    return(sym_list)