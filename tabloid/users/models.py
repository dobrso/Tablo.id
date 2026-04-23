from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    description = models.TextField('Описание')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль {self.user.username}'