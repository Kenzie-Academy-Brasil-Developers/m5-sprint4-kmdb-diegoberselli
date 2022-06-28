from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import CustonUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = None
    update_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustonUserManager()
    