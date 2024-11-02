from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('<str:username>/', views.user_home, name="user_home"),  # Dynamic URL pattern for user-specific home
]
