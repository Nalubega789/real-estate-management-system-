from django.http import HttpResponse

def index(request):
    return HttpResponse("Properties app is working!")
