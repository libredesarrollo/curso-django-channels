from django.urls import path

from . import views, api

urlpatterns = path('api/login',api.login),
urlpatterns += path('api/alerts',api.alerts),
urlpatterns += path('dashboard/alert',views.index),