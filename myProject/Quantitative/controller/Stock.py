# """股票类"""
from django.shortcuts import render
from django.http import HttpResponse
from .. modules import Stock, StockCompany
from .QuantAverBreak import QuantAverBreak
from .QuantTrendBreak import QuantTrendBreak
import json
import datetime


# """获取stack数据"""
def getStockData(request):
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
    resp = {
        "success": "ok",
        "data": json.loads(stock_data)
    }
    return resp

def getStockCompany(request):
    body = json.loads(request.body.decode())
    limit = int(body.get('limit'))
    pagenum = int(body.get('pagenum'))

    stock_company = StockCompany.getStockCompany('L', limit, pagenum)
    resp = {
        "code": 200,
        "data": {
            "msg": "成功",
            "data": stock_company
        }
    }
    return resp

def stockDataTest(request):
    stock_data = StockCompany.saveTsCodeWithCompany()

def strategyTrade(request):
    print("=======>")
    stock = Stock.Stock('BIDU', datetime.datetime(2014,1,1), datetime.date.today()).getStockData()
    print("get stock done")

    # example_trade = QuantAverBreak()
    # data = example_trade.run_factor_plot(stock)

    trend_break = QuantTrendBreak()
    data = trend_break.run_factor_plot(stock)
    resp = {
        "success": "ok",
        "code": 200,
        "data": data
    }
    return resp
