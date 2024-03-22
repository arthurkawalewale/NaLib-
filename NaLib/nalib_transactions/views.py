from django.shortcuts import render

# Create your views here.
def index(requests):

    ##catalogue = {'catalogue': Catalogue.objects.all()}
    return render(requests, 'nalib_transactions/lending.html')
