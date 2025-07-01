from django.contrib.auth.forms import UserCreationForm
from auth_custom.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User