from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model, login
from .models import Stuffs
from .forms import userRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
 
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')

def home_detail_view(request, user_id, *args, **kwargs):
    obj = Stuffs.objects.get(id = user_id)
    return HttpResponse(f'<h1>Hello {user_id} </h1>')

def login_view(request):
    if request.method == "POST":
        log_form = AuthenticationForm(data = request.POST)
        if log_form.is_valid():
            return redirect('/')
    else:
        log_form = AuthenticationForm()
    
    return render(
        request,
        template_name = 'login.html',
        context = {"form": log_form}
    )


def registration_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    
    else:
        form = userRegistrationForm()

    return render(
        request = request,
        template_name = "registration.html",
        context = {"form": form}
    )

def lobby_view(request, *args, **kwargs):
    return HttpResponse('<h1>Lobby Page</h1>')