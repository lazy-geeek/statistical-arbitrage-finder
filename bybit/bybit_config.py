from pybit.usdt_perpetual import HTTP, WebSocket

import toml

config = toml.load("./bybit/bybit_config.toml")

mode = "test"
timeframe = 60
kline_limit = 200
z_score_window = 21

api_key = config['testnet']['key'] if mode == "test" else config['mainnet']['key']
api_secret = config['testnet']['secret'] if mode == "test" else config['mainnet']['secret']

api_url = 'https://api-testnet.bybit.com' if mode == "test" else 'https://api.bybit.com'

session = HTTP(api_url, api_key, api_secret)

# test = mode == "test"

# ws = WebSocket(
#     test=test,
#     api_key=api_key,
#     api_secret=api_secret)
