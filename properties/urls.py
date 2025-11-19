from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartment_list, name='apartment_list'),
    path('apartments/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('apartments/<int:apartment_id>/book/', views.book_apartment, name='book_apartment'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
    template_name='login.html',
    next_page='apartment_list'
), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
