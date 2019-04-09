from django.shortcuts import render
from django.http import HttpResponse
import json
import datetime
from . import controller

# Create your views here.
def index(request):
    return HttpResponse('hello world')

# login
def login(request):
    return HttpResponse(json.dumps(controller.User.login(request)), content_type="application/json")
# register
def register(request):
    return HttpResponse(json.dumps(controller.User.register(request)), content_type="application/json")
# Loginout
def loginout(request):
    return HttpResponse(json.dumps(controller.User.loginout(request)), content_type="application/json")

# User
def setUserInfo(request):
    return HttpResponse(json.dumps(controller.User.setUserInfo(request)), content_type="application/json")




# 获取Stock数据
def getStockData(request):
    return HttpResponse(json.dumps(controller.Stock.getStockData(request)), content_type="application/json")

# 获取上市公司信息
def getStockCompany(request):
    return HttpResponse(json.dumps(controller.Stock.getStockCompany(request)), content_type="application/json")

def getStockCompanyDetail(request):
    return HttpResponse(json.dumps(controller.Stock.getStockCompanyDetail(request)), content_type="application/json")

# 搜索公司信息
def searchStockCompany(request):
    return HttpResponse(json.dumps(controller.Stock.searchStockCompany(request)), content_type="application/json")

# 存储股票数据测试
def stockDataTest(request):
    return HttpResponse(json.dumps(controller.Stock.stockDataTest(request)), content_type="application/json")

# 回测
def loopBack(request):
    runLoopBack = controller.RunLoopBack.RunLoopBack(request)
    return HttpResponse(json.dumps(runLoopBack.runLoopBack(request)), content_type="application/json")

def strategyTrade(request):
    # resp = controller.Stock.exampleTrade(request);
    resp = controller.Stock.strategyTrade(request);

    return HttpResponse(json.dumps(resp), content_type="application/json")