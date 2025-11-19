from django.contrib import admin
from Agent.models import Agent
from .models import Apartment, Booking


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available', 'owner')
    list_filter = ('available', 'location',)
    search_fields = ('title', 'location')


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "agent":
            kwargs["queryset"] = Agent.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'user', 'date_booked')
    list_filter = ('date_booked',)