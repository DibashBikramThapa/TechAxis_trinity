from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):

    name = models.fields.CharField(max_length=255)
    description = models.fields.CharField(max_length=255)
    created_at = models.fields.DateField(default=datetime.now())
    deadline = models.fields.DateField(blank=True, null=True)

    def __str__(self):
        return f""" name: {self.name}
                created_date:{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"""