from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='nalib-login'),
    path('register', views.register, name='user-registration')
]