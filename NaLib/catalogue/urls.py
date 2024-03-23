from django.urls import path
from .views import CatalogueListView, CatalogueCreateView, CatalogueUpdateView
from . import views

urlpatterns = [
    path('', CatalogueListView.as_view(), name='catalogue-home'),
    path('new/', CatalogueCreateView.as_view(), name='catalogue-create'),
    path('<int:pk>/update/', CatalogueUpdateView.as_view(), name='catalogue-update'),

]