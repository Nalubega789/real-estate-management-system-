from django.shortcuts import render, redirect
from .forms import InquiryForm
from .models import Inquiry


def inquiry_create(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_success')
    else:
        form = InquiryForm()

    return render(request, 'form.html', {'form': form})


def inquiry_success(request):
    return render(request, 'success.html')


def inquiry_list(request):
    all_data = Inquiry.__class__.objects.all().order_by('-created_at')
    return render(request, 'inquiry_list.html', {'inquiries': all_data})