import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from posts.models import Tag, Post

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='test', email='', password='')

@pytest.fixture
def tag(db):
    return Tag.objects.create(name='test_name')

@pytest.fixture
def post(db, user, tag):
    post = Post.objects.create(
        title='test_title',
        description='test_description',
        author=user,
    )
    post.tags.add(tag)
    return post

@pytest.mark.django_db
def test_posts_api_returns_list(api_client, post):
    url = reverse('posts:api_post_list')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['title'] == 'test_title'

@pytest.mark.django_db
def test_retrieve_post_api_returns_object(api_client, post, user):
    url = reverse('posts:api_post_detail', args=[post.id])
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200