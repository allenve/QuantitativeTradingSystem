# 动态实例化策略
import copy

buy_factors = [
    {'xd': 20, 'class': FactorBuyNDayBreak},
    {'xd': 30, 'class': FactorBuyAverBreak}
]

def init_buy_factors(self, buy_factors):
    self.buy_factors = list()

    if buy_factors is None:
        return

    for factor_class in buy_factors:
        if factor_class is None:
            continue
        if 'class' not in factor_class:
            raise ValueError('factor class key must name class')
        
        factor_class = copy.deepcopy(factor_class)

        class_fac = copy.deepcopy(factor_class['class'])

        del factor_class['class']

        factor = class_fac(**factor_class)

        if not isinstance(factor, FactorBuyAverBreak) and not isinstance(factor, FactorBuyNDayBreak):
            raise TypeError('factor must base FactorBuyBreak')

        self.buy_factors.append(factor)

def _day_task(self, kl_index, today):
    fact_buy,fact_sell,sell_buf,buy_buf = 0,0,0,0
    
    for index, buy_factor in enumerate(self.buy_factors):
        #遍历所有买入因子
        buy_buf += buy_factor.fit_day(kl_index, today, self.kl_pd)
    fact_buy = 1 if (buy_buf == (index+1)) else 0
    
    for index, sell_factor in enumerate(self.sell_factors):
        #遍历所有卖出因子
        sell_buf += sell_factor.fit_day(kl_index, today, self.kl_pd)
    fact_sell = -1 if (sell_buf > 0) else 0
    return fact_buy or fact_sell





def run_factor(self):
    for kl_index,today in self.kl_pd.iterrows():
        signal = self._day_task(kl_index, today)
        if signal > 0:# 买入
            if is_win == False:#空仓则买
                start = self.kl_pd.index.get_loc(kl_index)
                is_win = True
                self.posit_num = int(self.cash_hold/today.Close)
            
            elif signal < 0:# 卖出
                if is_win == True:#避免未买先卖
                    end = self.kl_pd.index.get_loc(kl_index)
                    is_win = False
                    print ("End order",kl_index)
                    self.cash_hold = int(self.posit_num*today.Close)
                    self.market_total = 0
                
            list_signal.append(is_win)
            if is_win == True:
                self.market_total = int(self.posit_num*today.Close)
                self.profit_curve.append(self.market_total)
            else:
                self.profit_curve.append(self.cash_hold)