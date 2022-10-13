from config_execution_api import mode
from config_execution_api import ticker_1
from config_execution_api import ticker_2

from pybit.usdt_perpetual import WebSocket

import time
from pprint import pprint

symbols = []
symbols.append(ticker_1)
symbols.append(ticker_2)

test = mode == "test"

ws = WebSocket(test=test)


