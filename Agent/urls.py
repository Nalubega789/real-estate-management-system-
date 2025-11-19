from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent_list'),
    path('<int:agent_id>/', views.agent_detail, name='agent_detail'),
    path('<int:agent_id>/contact/', views.contact_agent, name='contact_agent'),
path('manage-profile/', views.manage_agent_profile, name='manage_agent_profile'),
    path('dashboard/', views.agent_dashboard, name='agent_dashboard'),

]