from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.bloodbank, name="bloodbank"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path('<int:id>/', views.dashboard, name="dashboard"),
    path('<int:id>/logout', views.logout, name="logout"),
    path('<int:id>/update-stock', views.updateStock, name="update-stock"),
    path('<int:id>/edit-details', views.editDetails, name="edit-details"),
    path('<int:id>/change-password', views.changePassword, name="change-password"),
]