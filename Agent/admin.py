from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'email', 'phone')