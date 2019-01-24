# 历史数据回测
from .. modules import WidgetRunLoopBack
from .. abupy.WidgetBu.ABuWGBFBase import BuyFactorWGManager, WidgetFactorBuyBase


def runLoopBack(request):
    cash="1000000"
    choice_symbols=['usBIDU']

    bf = BuyFactorWGManager()
    buy = WidgetFactorBuyBase.add_buy_factor


    buy_factors = list(bf.factor_dict.values())

    print(buy_factors)

    return {"data": "12"}