from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.logins, name="login"),
    path('register', views.register, name="register"),
    path('travel', views.travel, name="travel"),
    path('go', views.go, name="go")
]
