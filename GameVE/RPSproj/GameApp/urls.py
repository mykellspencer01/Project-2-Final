from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('lobby/', views.lobby, name = 'lobby'),
    path('login/', auth_view.LoginView.as_view(template_name = 'html/login.html'), name = 'login'),
    path('logout/', auth_view.LoginView.as_view(template_name = 'html/logout.html'), name = 'logout'),
]
