import pytest
from django.contrib.auth import get_user_model

from posts.models import Tag, Post
from users.models import Profile

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='test', email='', password='')

@pytest.fixture
def tag(db):
    return Tag.objects.create(name='test_tag')

@pytest.fixture
def another_tag(db):
    return Tag.objects.create(name='another_tag')

class TestTag:
    def test_create_tag(self, db):
        tag = Tag.objects.create(name='test_tag')
        assert tag.name == 'test_tag'
        assert str(tag) == 'test_tag'

class TestPost:
    def test_create_post(self, user, tag):
        post = Post.objects.create(
            title='test_title',
            description='test_description',
            author=user,
        )
        post.tags.add(tag)
        assert post.title == 'test_title'
        assert post.description == 'test_description'
        assert post.author == user
        assert post.tags.count() == 1

    def test_post_with_multiple_tags(self, user, tag, another_tag):
        post = Post.objects.create(
            title='test_title',
            description='test_description',
            author=user,
        )
        post.tags.add(tag, another_tag)
        assert post.tags.count() == 2

class TestProfile:
    def test_profile_created_automatically(self, db):
        user = User.objects.create_user(username='test', email='', password='')
        assert Profile.objects.filter(user=user).exists()

    def test_profile_description_field(self, user):
        profile = Profile.objects.get(user=user)
        assert profile.description == ''

        profile.description = 'updated description'
        profile.save()

        updated_profile = Profile.objects.get(user=user)
        assert updated_profile.description == 'updated description'