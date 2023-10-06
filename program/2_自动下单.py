"""
《邢不行 | 数字货币量化实操营》
邢不行微信: xbx2626
本程序作者: 邢不行
"""
#必看！！！！注意自动下单必须用vpn或翻墙后才能正常使用。
import ccxt
import time
import pandas as pd
pd.set_option("display.max_rows", 1000)
pd.set_option('expand_frame_repr', False)


# =====币安自动交易配置
p = { 'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890', } 
exchange = ccxt.binance({'proxies': p})
exchange.apiKey = ''  # 填写APIkey
exchange.secret = ''  # 填写secret


# =====查询账户余额
# 获取余额信息
balance = exchange.private_getV2_account()
print(balance)
# 整理信息
df = pd.DataFrame(balance['balances'])


# =====自动下单交易
# 指定下单币种
symbol = 'BTCUSDT'  # 可以尝试其他的币种
# 指定下单数量
quantity = 0.1
# 指定下单价格
price = 25000
# 下单
exchange.private_post_order(
    params={'symbol': symbol, 'quantity': quantity, 'price': price,
            'side': 'BUY', 'type': 'LIMIT',
            'timeInForce': 'GTC', 'timestamp': int(time.time()) * 1000}
)


# =====自动撤单
# 指定撤单币种
symbol = 'BTCUSDT'
exchange.private_delete_openorders(
    params={'symbol': symbol, 'timestamp': int(time.time()) * 1000}
)
