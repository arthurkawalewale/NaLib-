from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def login(request):
    #return HttpResponse('<h1>Welcome to Nalib</h1>')
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('catalogue-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/registeration.html', {'form':form})
