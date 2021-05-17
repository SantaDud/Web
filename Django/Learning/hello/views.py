from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello!")

def random(request, name):
    return render(request, 'hello/new.html', {
        "name": name.capitalize()
    })