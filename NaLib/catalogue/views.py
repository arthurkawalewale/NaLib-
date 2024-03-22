from django.shortcuts import render
from .models import Catalogue

# Create your views here.
def index(requests):

    catalogue = {'catalogue': Catalogue.objects.all()}
    return render(requests, 'catalogue/catalogue.html', catalogue)
