
from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_joined', 'is_active']
    list_filter = ['is_active', 'date_joined']
    search_fields = ['name', 'email']