from func_calcultions import get_trade_details
from config_ws_connect import ws, symbols

def handle_orderbook(message):
    orderbook_data = message["data"]
    symbol, mid_price, stop_loss, quantity = get_trade_details(orderbook_data, capital=1000)
    print(symbol, mid_price, stop_loss, quantity)
    
ws.orderbook_25_stream(handle_orderbook, symbols)


while True:
    pass

