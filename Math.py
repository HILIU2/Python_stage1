stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}  #不能sort 股价,只能sort 股票的名字

print('sorted items in values', sorted(zip(stocks.values(), stocks.keys())))  # sorted() 对zip的第一个参数进行排列

print('sorted items alphabetically', sorted(zip(stocks.keys(), stocks.values())))

print('print the minimum', min(zip(stocks.keys(), stocks.values())))
