from django.shortcuts import render, redirect
from .forms import InquiryForm
from django.http import HttpResponse


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
    return render(request, 'success.html')  # Updated to use template


def inquiry_list(request):
    return HttpResponse("Inquiries list page")  # Keep this as is for now