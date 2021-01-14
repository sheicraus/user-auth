from django.contrib import admin
from django.urls import path
from .views import HomePageView
from helloapp import views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('signup/', views.SignUpView, name="signup"),
]
