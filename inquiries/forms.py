from django import forms
from .models import Inquiries

class InquiryForm(forms.Form):
    class Meta:
        model = Inquiries
        fields = ['name','email','message']