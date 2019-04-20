from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField(upload_to='icons/')
    bio = models.CharField(max_length=200)
