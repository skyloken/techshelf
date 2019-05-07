from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField('アイコン', upload_to='icons/', default='icons/default.png')
    bio = models.CharField('バイオグラフィー', max_length=200, blank=True, null=True)
