from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "common"
urlpatterns = [
    path('', views.index),
]
