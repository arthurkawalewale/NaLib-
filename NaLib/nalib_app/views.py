from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Nalib</h1>')
    return render(request, 'nalib_app/home.html')