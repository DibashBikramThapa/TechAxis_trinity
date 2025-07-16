from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy

from auth_custom.forms import MyUserCreationForm


class MyLoginView(LoginView):
    template_name = 'auth_custom/login.html'


class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = 'auth_custom/signup.html'
    success_url = reverse_lazy('login')