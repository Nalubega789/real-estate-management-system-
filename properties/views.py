from django.shortcuts import render, get_object_or_404, redirect  # Add redirect here
from django.http import HttpResponse
from .models import Apartment, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    apartments = Apartment.objects.filter(available=True)
    return render(request, 'home.html', {'apartments': apartments})

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'properties/apartment_list.html', {'apartments': apartments})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'properties/apartment_detail.html', {'apartment': apartment})


@login_required
def book_Apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        message = request.POST.get('message', '')
        Booking.objects.create(apartment=apartment, user=request.user, message=message)
        apartment.available = False
        apartment.save()
        return redirect('apartment_list')  # Also fixed the name to match my URL pattern
    return render(request, 'properties/book_property.html', {'apartment': apartment})