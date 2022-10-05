from bybit_config import session
from bybit_config import timeframe
from bybit_config import kline_limit

import datetime
import time

if timeframe == 60:
    time_start_date = datetime.datetime.now() - datetime.timedelta(hours=kline_limit)
if timeframe == "D":
    time_start_date = datetime.datetime.now() - datetime.timedelta(days=kline_limit)
time_start_seconds = int(time_start_date.timestamp()) # type: ignore

# Get historical prices (klines)
def get_price_klines(symbol):

    # Get prices
    prices = session.query_mark_price_kline(
        symbol = symbol,
        interval = timeframe,
        limit = kline_limit,
        from_time = time_start_seconds
    )

    # Manage API calls
    time.sleep(0.1)

    # Return output
    if len(prices["result"]) != kline_limit:
        return []
    return prices["result"]