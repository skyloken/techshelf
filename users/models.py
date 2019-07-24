from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField('アイコン', upload_to='icons/', default='icons/default.png')
    bio = models.TextField('バイオグラフィー', blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(id=self.id)
            if this.icon != self.icon:
                this.icon.delete(save=False)
        except self.DoesNotExist:
            pass
        super(User, self).save(*args, **kwargs)
