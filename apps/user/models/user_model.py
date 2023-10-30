from django.db import models
from django.contrib.auth.models import AbstractUser
from .rol_model import Rol
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','rol']
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.email
