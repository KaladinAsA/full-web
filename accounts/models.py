from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """creating new&cutom fields"""
    age = models.PositiveIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile/',blank=True, null=True)
