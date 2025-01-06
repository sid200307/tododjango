from django.db import models
from django.contrib.auth.models import User  # Corrected import

# Create your models here.

class todo(models.Model):  # Class names should follow the PEP 8 convention (CamelCase)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected to use User
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)  

    def __str__(self):
        return self.name  # Corrected the return to use 'name' instead of 'todo_name'
