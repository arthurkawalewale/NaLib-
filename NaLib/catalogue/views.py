from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Catalogue
from django.urls import reverse_lazy

# Create your views here.
"""def index(requests): #returns view listing all the resources in the catalogue

    catalogue = {'catalogue': Catalogue.objects.all()}
    return render(requests, 'catalogue/catalogue.html', catalogue)
"""

class CatalogueListView(ListView): #returns view listing all the resources in the catalogue
    model = Catalogue
    template_name = 'catalogue/catalogue.html'
    context_object_name = 'catalogue'

class CatalogueDetailView(DetailView):
    pass

class CatalogueCreateView(CreateView):
    model = Catalogue
    fields = ['title', 'author', 'ISBN', 'Type', 'Category', 'YearPublished']
    success_url = '/catalogue'

class CatalogueUpdateView(UpdateView):
    model = Catalogue
    fields = ['title', 'author', 'ISBN', 'Type', 'Category', 'YearPublished']

class CatalogueDeleteView(DeleteView):
    pass