from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('getStockData/', views.getStockData, name='post_case'),
    path('loopBack/', views.loopBack, name="get_case"),
    path('strategyTrade/', views.strategyTrade, name="get_case")

]