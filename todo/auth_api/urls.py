from django.urls import path
from auth_api.views import CustomAuthToken

urlpatterns = [
    path('login', CustomAuthToken.as_view()),
]
