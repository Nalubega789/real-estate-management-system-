from django.shortcuts import render
from .forms import InquiryForm


def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = InquiryForm()

    return render(request, 'base.html', {'form': form})