from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )