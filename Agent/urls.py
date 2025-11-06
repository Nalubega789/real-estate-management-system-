from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='agents_index'),
    path('list/', views.agents_list, name='agents_list'),
]


