from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Apartment, Booking
from .forms import UserRegisterForm  

def home(request):
    return render(request, 'home.html')

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'properties/apartment_list.html', {'apartments': apartments})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'properties/apartment_detail.html', {'apartment': apartment})

@login_required
def book_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        message = request.POST.get('message', '')
        Booking.objects.create(apartment=apartment, user=request.user, message=message)
        apartment.available = False
        apartment.save()
        return redirect('apartment_list')
    return render(request, 'properties/book_property.html', {'apartment': apartment})

#  this view  is for registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})