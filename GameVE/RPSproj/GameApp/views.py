from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Stuffs
 
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')

def home_detail_view(request, user_id, *args, **kwargs):
    obj = Stuffs.objects.get(id = user_id)
    return HttpResponse(f'<h1>Hello {user_id} </h1>')
#- {obj.content}
def login_view(request, *args, **kwargs):
    return HttpResponse('<h1>Login Page</h1>')

def registration_view(request, *args, **kwargs):
    return HttpResponse('<h1>Registration Page</h1>')

def lobby_view(request, *args, **kwargs):
    return HttpResponse('<h1>Lobby Page</h1>')