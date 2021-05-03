from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital, name="hospital"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/findblood', views.findblood, name="findblood"),
]