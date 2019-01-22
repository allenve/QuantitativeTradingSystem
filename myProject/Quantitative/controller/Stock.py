"""股票类"""
from django.shortcuts import render
from django.http import HttpResponse
from .. modules import Stock
import json
import datetime


"""获取stack数据"""
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



def main():
    print("main()")