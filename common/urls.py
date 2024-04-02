from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', LoginView.as_view(template_name = "/common/login.html"), name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
]
