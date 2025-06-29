from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    template_name = 'auth_custom/login.html'
