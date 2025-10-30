from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Apartment

def home(request):
    apartments = Apartment.objects.filter(available=True)
    return render(request, 'home.html', {'apartments': apartments})

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'properties/apartment_list.html', {'apartments': apartments})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'apartment_detail.html', {'apartment': apartment})
