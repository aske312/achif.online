# -*- coding: utf-8 -*-
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='default-Index'),
]
