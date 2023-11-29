from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
def home(request):
    return render(request, 'html/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account was created successfully!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'html/registration.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'html/profile.html')

@login_required
def lobby(request):
    return render(request, 'html/lobby.html')