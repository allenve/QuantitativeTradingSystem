# QuantAverBreak 单均线突破
import numpy as np
import datetime
import time

class QuantAverBreak:
    def __init__(self):
        self.skip_days = 0
        self.cash_hold = 100000#初始资金
        self.posit_num = 0#持股数目
        self.market_total = 0#持股市值
        self.profit_curve = []
    def run_factor_plot(self, stock_df):
        stock_df['Ma60'] = stock_df.Close.rolling(window=60).mean()#增加M60移动平均线
        list_diff = np.sign(stock_df.Close-stock_df.Ma60)
        stock_df['signal'] = np.sign(list_diff-list_diff.shift(1))
        
        buyDay = []
        sellDay = []
        for kl_index,today in stock_df.iterrows():
            if today.signal > 0:# 买入
                print("buy", kl_index)
                buyDay.append(str(kl_index.to_pydatetime()))
                self.skip_days = -1
                self.posit_num = int(self.cash_hold/today.Close)
                self.cash_hold = 0
            elif today.signal < 0:# 卖出
                if self.skip_days == -1:#避免未买先卖
                    print("sell", kl_index)
                    sellDay.append(str(kl_index.to_pydatetime()))
                    self.skip_days = 0
                    self.cash_hold = int(self.posit_num*today.Close)
                    self.market_total = 0


            if self.skip_days == -1:
                self.market_total = int(self.posit_num*today.Close)
                self.profit_curve.append(self.market_total)

            else:
                self.profit_curve.append(self.cash_hold)

            
            
        resp = {
            "buy": buyDay, "sell": sellDay
        }
        return resp
