from StockDataMod import GetStockDatPro
# from IndicatStrateMod import QuantPickTimeSys, FactorBuyNdayBreak, FactorBuyAverBreak, FactorSellNdayBreak, FactorSellAverBreak, FactorSellAtrStop
from AtrStrateMod import QuantPickTimeSys, FactorBuyNdayBreak, FactorBuyAverBreak, FactorSellNdayBreak, FactorSellAverBreak, FactorSellAtrStop

code = "000004.SZ"
start="2018-04-17"
end="2019-04-17"

df_stockload = GetStockDatPro(code, start, end)

buy_factors = [{'xd': 20,'class': FactorBuyNdayBreak},
               {'xd': 30,'class': FactorBuyAverBreak}]

sell_factors = [{'xd': 5,'class': FactorSellNdayBreak},
                {'xd': 30,'class': FactorSellAverBreak},
                {'stop_loss_n': 0.8,'stop_win_n': 2,'class': FactorSellAtrStop}]
# 获取策略结果
print('data get')
examp_trade= QuantPickTimeSys(df_stockload,buy_factors,sell_factors)
factor_result = examp_trade.run_factor_plot()

# print(factor_result)
print('ok')