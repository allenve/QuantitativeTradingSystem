# N日

class FactorSellNdayBreak:
    def __init__(self, **kwargs):
        self.xd = kwargs['xd']

    def fit_day(self, kl_index, today, stock_df):
        day_ind = stock_df.index.get_loc(kl_index)

        if day_ind < self.xd - 1 or day_ind >= stock_df.shape[0] - 1:
            return False
        
        if today.Close == stock_df.Close[day_ind - self.xd + 1:day_ind + 1].min():
            print('FactorSellNdayBreak', kl_index, today.Close, stock_df.Close[day_ind - self.xd + 1:day_ind + 1].min())

            return self.fit_sell_order()

        return False

    def fit_sell_order(self):
        sell_signal = True
        return sell_signal
