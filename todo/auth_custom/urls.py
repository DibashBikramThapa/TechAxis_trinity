from django.urls import path
from auth_custom.views import MyLoginView, LogoutView

urlpatterns = [
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='my_logout'),
]
