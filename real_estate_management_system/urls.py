from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Real Estate Management System!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('properties.urls')),
    path('listings/', include('listings.urls')),
    path('Agent/', include('Agent.urls')),
    path('Inquiry/', include('Inquiry.urls')),
    path('bookings/', include('bookings.urls')),

    path('', home, name='home'),
]
