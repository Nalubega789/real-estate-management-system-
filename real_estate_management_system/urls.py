from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return HttpResponse("Welcome to the Real Estate Management System!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('properties.urls')),
    path('listings/', include('listings.urls')),
    path('agents/', include('agents.urls')),
    path('inquiries/', include('inquiries.urls')),
    path('bookings/', include('bookings.urls')),

    path('', home, name='home'), 
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('properties.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
