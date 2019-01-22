"""Stock 类"""

import pandas as pd
import numpy as np
import pandas_datareader.data as web


class Stock:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def getStockFromHttp(self):
        # 获取数据
        prices = web.DataReader(self.name, 'yahoo', self.start, self.end)
        # 处理缺失值
        prices = prices.dropna(axis=0,how='all')
        # 保留2位小数
        prices = prices.round(2)
        # 转换为json数据
        prices = prices.to_json(orient="index")

        return prices