from django.urls import path
from .views import * # Get all views from user > views
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup),
]
