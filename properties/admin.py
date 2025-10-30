from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available')
    list_filter = ('available', 'location')
    search_fields = ('title', 'location')
