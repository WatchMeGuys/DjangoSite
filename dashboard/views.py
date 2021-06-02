from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import AuthUserForm, RegisterUserForm

def index(request):
    return render(request, 'dashboard/index.html')


def register(request):
    return render(request, 'dashboard/register.html')


class Login(LoginView):
    fields = ['username', 'password']
    template_name = 'dashboard/login.html'
    form_class = AuthUserForm


class Logout(LogoutView):
    template_name = 'dashboard/logout.html'


class Register(CreateView):
    model = User
    template_name = 'dashboard/register.html'
    form_class = RegisterUserForm
    success_url = '/'


