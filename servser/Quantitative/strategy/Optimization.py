#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# author pythontab.com


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


#场外篇 单均线参数最优化
class QuantAverBreak:
    def __init__(self):
        self.skip_days = 0
        self.cash_hold = 100000  # 初始资金
        self.posit_num = 0  # 持股数目
        self.market_total = 0  # 持股市值
        self.profit_curve = []

    def run_factor_plot(self, stock_df, N):

        stock_df['Ma_n'] = stock_df.Close.rolling(window=N).mean()  # 增加M60移动平均线
        list_diff = np.sign(stock_df.Close - stock_df.Ma_n)
        stock_df['signal'] = np.sign(list_diff - list_diff.shift(1))

        for kl_index, today in stock_df.iterrows():
            # print "kl_index",kl_index
            # print "today",today
            if today.signal > 0:  # 买入
                #print("buy", kl_index)
                start = stock_df.index.get_loc(kl_index)
                self.skip_days = -1
                self.posit_num = int(self.cash_hold / today.Close)
                self.cash_hold = 0
            elif today.signal < 0:  # 卖出
                if self.skip_days == -1:  # 避免未买先卖
                    #print("sell", kl_index)
                    end = stock_df.index.get_loc(kl_index)
                    self.skip_days = 0
                    self.cash_hold = int(self.posit_num * today.Close)
                    self.market_total = 0
            if self.skip_days == -1:
                self.market_total = int(self.posit_num * today.Close)
                self.profit_curve.append(self.market_total)
            else:
                self.profit_curve.append(self.cash_hold)
        stock_df['profit'] = self.profit_curve
        return stock_df['profit'][-1]

stock = web.DataReader("600797.SS", "yahoo", datetime.datetime(2017, 1, 1), datetime.date.today())

plt.figure(figsize=(25, 12), dpi=80, facecolor="white")
ma_list = []
profit_list = []
for ma in range(20, 60):
    examp_trade = QuantAverBreak()
    ma_list.append(ma)
    profit_list.append(examp_trade.run_factor_plot(stock, ma))

profit_max=max(profit_list)
print(profit_list.index(max(profit_list)))
ma_max=ma_list[profit_list.index(max(profit_list))]
plt.bar(ma_list, profit_list)
plt.annotate('最优参数ma='+str(ma_max)+'\n profit='+str(profit_max),\
             xy=(ma_max,profit_max),xytext=(ma_max-10, profit_max-10),arrowprops=dict(facecolor='yellow',shrink=0.1),\
             horizontalalignment='left',verticalalignment='top',fontsize=20)
# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 设置坐标标签字体大小
plt.xlabel('均线参数',fontsize=20)
plt.ylabel('资金收益',fontsize=20)
# 设置坐标轴的取值范围
plt.xlim(min(ma_list)-1, max(ma_list)+1)
plt.ylim(min(profit_list)*0.99, max(profit_list)*1.01)
# 设置x坐标轴刻度
plt.xticks(np.arange(min(ma_list), max(ma_list)+1, 1))
# 设置图例字体大小
plt.legend(['profit_list'], loc='best', fontsize=20)
plt.title("均线最优参数",fontsize=50)
plt.show()




