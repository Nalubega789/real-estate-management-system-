from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Agents app is working!")

def agents_list(request):
    agents = [
        {'name':'', 'email':'', 'phone':'' },
        {'name': '', 'email': '','phone':''},
    ]
    return render(request, 'list.html', {'agents': agents})