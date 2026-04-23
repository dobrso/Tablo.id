from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name='Тэги')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title