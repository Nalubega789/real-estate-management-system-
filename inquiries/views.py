from django.http import HttpResponse

def index(request):
    return HttpResponse("Inquiries app is working!")
