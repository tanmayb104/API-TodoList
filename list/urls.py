  
from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.itemslist, name="itemslist"),
    path('create/', views.create, name="create"),
    path('delete/<str:pk>', views.delete, name="delete"),
]