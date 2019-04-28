# """股票类"""
from django.shortcuts import render
from django.http import HttpResponse
from .. modules import Stock, StockCompany
from .QuantAverBreak import QuantAverBreak
from .QuantTrendBreak import QuantTrendBreak
import json
import datetime


# 获取stack数据
def getStockData(request):
    body = json.loads(request.body.decode())
    code = body.get('code')
    start = body.get('start')
    end = body.get('end')

    print(code, start, end)
    stock = Stock.Stock(code, start, end)
    resp = {
        "success": "ok",
        "data": json.loads(stock.getStockFromHttp())
    }
    return resp

def getStockCompany(request):
    body = json.loads(request.body.decode())
    limit = int(body.get('limit'))
    pagenum = int(body.get('pagenum'))

    stock_company = StockCompany.getStockCompany('L', limit, pagenum)
    resp = {
        "code": stock_company[0],
        "data": stock_company[1]
    }
    return resp

def searchStockCompany(request):
    body = json.loads(request.body.decode())
    name = body.get('name')

    stock_company = StockCompany.searchStockCompanyByName(name)
    resp = {
        "code": stock_company[0],
        "data": stock_company[1]
    }
    return resp

def getStockCompanyDetail(request):
    body = json.loads(request.body.decode())
    ts_code = body.get('ts_code')

    stock_company_detail = StockCompany.searchStockCompanyByTsCode(ts_code)
    resp = {
        "code": stock_company_detail[0],
        "data": stock_company_detail[1]
    }
    return resp








# 测试
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
