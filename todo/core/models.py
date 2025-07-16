from django.db import models
from auth_custom.models import User
# Create your models here.

class Todo(models.Model):

    name = models.fields.CharField(max_length=255)
    description = models.fields.CharField(max_length=255)
    created_at = models.fields.DateField(auto_now_add=True)
    deadline = models.fields.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f""" name: {self.name}
                created_date:{self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None}"""