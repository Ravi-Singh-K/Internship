from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    contact = models.CharField(unique=True, max_length=15)
    is_contact_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []