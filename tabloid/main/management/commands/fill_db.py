from random import choice

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from users.models import Profile
from posts.models import Tag, Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = self._create_users()
        tags = self._create_tags()
        self._create_posts(tags, users)

        self.stdout.write(self.style.SUCCESS('БД заполнена данными'))

    def _create_users(self):
        User = get_user_model()
        users = []

        if not User.objects.filter(username='tabloadmin').exists():
            admin = User.objects.create_superuser(username='tabloadmin', email='tabloadmin@example.com', password='tabloadmin')
            Profile.objects.create(user=admin)
            self.stdout.write('Создан superuser')

        for i in range(5):
            user, created = User.objects.get_or_create(username=f'tabloid_{i+1}', defaults={'email': f'tabloid_{i+1}@example.com'})

            if created:
                user.set_password(f'tabloid_{i+1}')
                user.save()
                Profile.objects.create(user=user)
                self.stdout.write(f'Создан user: {user.username}')
            users.append(user)
        return users

    def _create_tags(self):
        names = ['Угар', 'Трукрайм', 'Завоз', 'Фигня']
        tags = []

        for name in names:
            tag = Tag.objects.get_or_create(name=name)
            tags.append(tag)

        self.stdout.write('Созданы tags')
        return tags

    def _create_posts(self, tags, users):
        titles = ['Завозящий заголовок', 'Рофельный заголовок', 'Грустный заголовок']

        for i in range(10):
            tag = choice(tags)
            post, _ = Post.objects.get_or_create(
                title=choice(titles),
                description='Информативное описание',
                author=choice(users),
            )
            post.tags.add(choice(tags))

        self.stdout.write('Созданы posts')
