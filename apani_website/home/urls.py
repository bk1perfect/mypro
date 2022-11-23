from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index1", views.index1, name='index1.html'),
    path("index2", views.index2, name='index2.html'),
    path("index3", views.index3, name='index3.html'),
]
