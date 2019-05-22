# 
from django.http import HttpResponse
from .. strategy.StockDataMod import GetStockDatPro
# from .. strategy.IndicatStrateMod import QuantPickTimeSys, FactorBuyNdayBreak, FactorBuyAverBreak, FactorSellNdayBreak, FactorSellAverBreak, FactorSellAtrStop
from .. strategy.AtrStrateMod import QuantPickTimeSys, FactorBuyNdayBreak, FactorBuyAverBreak, FactorSellNdayBreak, FactorSellAverBreak, FactorSellAtrStop
import json

def runStrategy(request):
    body = json.loads(request.body.decode())
    code = body.get('selectedCompany')
    start = body.get('start')
    end = body.get('end')
    # read_cash = body.get('read_cash')
    # factors = body.get('selectedFactors')

    # 获取股票数据
    df_stockload = GetStockDatPro(code, start, end)

    # =====================
    buy_factors = [{'xd': 20,'class': FactorBuyNdayBreak},
               {'xd': 30,'class': FactorBuyAverBreak}]

    sell_factors = [{'xd': 5,'class': FactorSellNdayBreak},
                {'xd': 30,'class': FactorSellAverBreak},
                {'stop_loss_n': 0.8,'stop_win_n': 2,'class': FactorSellAtrStop}]
    # 获取策略结果
    examp_trade= QuantPickTimeSys(df_stockload, buy_factors, sell_factors)
    factor_result = examp_trade.run_factor_plot()
    return {
        'code': 200,
        'data': factor_result
    }


    