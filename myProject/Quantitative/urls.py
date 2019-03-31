from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('index/', views.index),
    # 登录注册
    path('register/', views.register, name='post_case'),
    path('login/', views.login, name='post_case'),
    path('loginout/', views.loginout, name='get_case'),

    # User
    path('setUserInfo/', views.setUserInfo, name='post_case'),

    # Stock
    # 搜索股票公司信息
    path('getStockCompany/', views.getStockCompany, name='post_case'),
    path('stockDataTest/', views.stockDataTest, name='post_case'),

    path('getStockData/', views.getStockData, name='post_case'),
    path('loopBack/', views.loopBack, name="get_case"),
    path('strategyTrade/', views.strategyTrade, name="get_case")

]