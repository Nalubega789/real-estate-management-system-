from django.contrib import admin
from .models import Apartment, Booking

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available')
    list_filter = ('available', 'location')
    search_fields = ('title', 'location')

    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'user', 'date_booked')
    list_filter = ('date_booked',)
