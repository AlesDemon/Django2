from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios/', userView.as_view())
]