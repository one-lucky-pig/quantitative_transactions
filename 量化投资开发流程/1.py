import akshare as ak

get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date", var="RB", start_day="20180618", end_day="20180718")
print(get_roll_yield_bar_df)
print(ak.get_cffex_daily(date="20100416"))


stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="601398", indicator="分红", date="2019-07-08")
print(stock_history_dividend_detail_df)
stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="601398", indicator="分红", date="2019-07-08")

print(stock_history_dividend_detail_df)

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol="601398", indicator="分红")
print(stock_history_dividend_detail_df)