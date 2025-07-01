from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'user'