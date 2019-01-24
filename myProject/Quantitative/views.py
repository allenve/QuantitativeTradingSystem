from django.shortcuts import render
from django.http import HttpResponse
import json
import datetime
from . import controller

# Create your views here.
def index(request):
    return HttpResponse('hello world')

"""获取Stock数据"""
def getStockData(request):
    return HttpResponse(json.dumps(controller.Stock.getStockData(request)), content_type="application/json")

def loopBack(request):
    return HttpResponse(json.dumps(controller.RunLoopBack.runLoopBack(request)), content_type="application/json")

def strategyTrade(request):
    # resp = controller.Stock.exampleTrade(request);
    resp = controller.Stock.strategyTrade(request);

    return HttpResponse(json.dumps(resp), content_type="application/json")