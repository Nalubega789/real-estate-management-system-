from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.apartment_list, name='apartment_list'),
    path('apartments/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('apartments/<int:apartment_id>/book/', views.book_apartment, name='book_apartment'),
]
