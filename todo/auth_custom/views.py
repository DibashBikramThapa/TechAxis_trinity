from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    template_name = 'auth_custom/login.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'auth_custom/signup.html'
    success_url = reverse_lazy('login')