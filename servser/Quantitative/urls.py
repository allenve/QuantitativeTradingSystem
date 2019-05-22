from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token
from .import views

urlpatterns = [
    path('index/', views.index),

    # User
    path('register', views.register, name='post_case'),
    path('login', views.login, name='post_case'),
    path('loginout', views.loginout, name='get_case'),
    path('setUserInfo', views.setUserInfo, name='post_case'),
    path('changePsd', views.changePassword, name='post_case'),

    # 查询模块
    path('getStockCompany', views.getStockCompany, name='post_case'),
    path('getStockCompanyDetail', views.getStockCompanyDetail, name='post_case'),
    path('searchStockCompany', views.searchStockCompany, name='post_case'),
    path('getStockData', views.getStockData, name='post_case'),


    # 收藏模块
    path('collectionCompany', views.collectionCompany, name="post_case"),
    path('isCompanyCollection', views.isCompanyCollection, name="post_case"),
    path('cancelCollectionCompany', views.cancelCollectionCompany, name="post_case"),
    path('getUserColledCompany', views.getUserCollectCompany, name="post_case"),

    # 回测    
    path('runStrategy', views.runStrategy, name="post_case"),



    path('stockDataTest', views.stockDataTest, name='post_case'),
    
    path('loopBack/', views.loopBack, name="get_case"),
    path('strategyTrade/', views.strategyTrade, name="get_case")

]