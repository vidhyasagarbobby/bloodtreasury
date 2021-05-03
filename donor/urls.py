from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.donor),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path('<str:username>/', views.dashboard, name="dashboard"),
    path('<str:username>/logout', views.logout, name="logout"),
    path('<str:username>/update-history', views.updateHistory, name="update-history"),
    path('<str:username>/edit-details', views.editDetails, name="edit-details"),
    path('<str:username>/change-password', views.changePassword, name="change-password"),
]