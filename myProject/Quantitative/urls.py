from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('getStockData/', views.getStockData, name='post_case')
]