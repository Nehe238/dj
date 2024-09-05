"""app1의URL정의"""
from django.urls import path
from .apps import App1Config as config
from . import views as v

app_name = config.name # app1가 들어있다.
urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('app/', v.ApplicationView.as_view(), name='app'), # 추가
]
