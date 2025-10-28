from django.http import HttpResponse

def index(request):
    return HttpResponse("Users app is working!")
from django.shortcuts import render

# Create your views here.
