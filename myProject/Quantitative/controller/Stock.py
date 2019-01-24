# """股票类"""
from django.shortcuts import render
from django.http import HttpResponse
from .. modules import Stock
from .QuantAverBreak import QuantAverBreak
from .QuantTrendBreak import QuantTrendBreak
import json
import datetime

# """获取stack数据"""
def getStockData(request):
    print("post requet")
    print(request.body)
    body = json.loads(request.body.decode())
    code = body.get('code')
    start = body.get('start')
    # start = datetime.datetime(2019, 1, 1)
    end = body.get('end')

    print(code, start, end)
    stock = Stock.Stock(code, start, end)
    resp = {
        "success": "ok",
        "data": json.loads(stock.getStockFromHttp())
    }
    return resp


def strategyTrade(request):
    print("=======>")
    stock = Stock.Stock('BIDU', datetime.datetime(2017,1,1), datetime.date.today()).getStockData()
    print("get stock done")

    # example_trade = QuantAverBreak()
    # data = example_trade.run_factor_plot(stock)

    trend_break = QuantTrendBreak()
    data = trend_break.run_factor_plot(stock)
    resp = {
        "success": "ok",
        "data": data
    }
    return resp

def main():
    print("main()")