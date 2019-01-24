# N日趋势突破

import numpy as np
import datetime
import time
import json

class QuantTrendBreak:
    def __init__(self):
        self.skip_days = 0
        self.cash_hold = 100000#初始资金
        self.posit_num = 0#持股数目
        self.market_total = 0#持股市值
        self.profit_curve = []
    def run_factor_plot(self, stock_df):
        N1 = 22
        N2 = 11
        stock_df['N1_High'] = stock_df.High.rolling(window=N1).max()#计算最近N1个交易日最高价
        expan_max = stock_df.Close.expanding().max()
        stock_df['N1_High'].fillna(value=expan_max,inplace=True)#目前出现过的最大值填充前N1个nan
        stock_df['N2_Low'] = stock_df.Low.rolling(window=N2).max()#计算最近N2个交易日最低价
        expan_min = stock_df.Close.expanding().max()
        stock_df['N2_Low'].fillna(value=expan_min,inplace=True)#目前出现过的最小值填充前N2个nan
        #""" 收盘价超过N1最高价 买入股票持有"""
        buy_index = stock_df[stock_df.Close > stock_df.N1_High.shift(1)].index #报错 TypeError
        stock_df.loc[buy_index,'signal'] = 1
        #""" 收盘价超过N2最低价 卖出股票持有"""
        sell_index = stock_df[stock_df.Close < stock_df.N2_Low.shift(1)].index #报错 TypeError
        stock_df.loc[sell_index,'signal'] = 0
        stock_df['keep'] = stock_df.signal.shift(1)
        stock_df['keep'].fillna(method = 'ffill',inplace = True)
        #""" 计算基准收益 """
        stock_df['benchmark_profit'] = np.log(stock_df.Close/stock_df.Close.shift(1))

        #print('benchmark_profit',stock_df['benchmark_profit'])
        #""" 计算趋势突破策略收益 """
        stock_df['trend_profit'] = stock_df.keep*stock_df.benchmark_profit
        #""" 可视化收益情况对比 """
        stock_df['watsignal'] = np.sign(stock_df['keep']-stock_df['keep'].shift(1))
        
        buyDay = []
        sellDay = []
        for kl_index,today in stock_df.iterrows():
            if today.watsignal == 1:# 买入
                self.skip_days = -1
                buyDay.append(str(kl_index.to_pydatetime()))
            elif today.watsignal == -1:# 卖出
                if self.skip_days == -1:
                    self.skip_days = 0
                    sellDay.append(str(kl_index.to_pydatetime()))

        stock = stock_df.to_json(orient="index")

        print(stock)

        resp = {
            "stock": json.loads(stock),
            "date": {
                "buy": buyDay, "sell": sellDay
            }
        }

        return resp