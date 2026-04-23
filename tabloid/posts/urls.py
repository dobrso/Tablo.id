from django.urls import path

from .api_views import PostListAPIView, PostRetrieveAPIView
from .views import post_list, post_create, post_detail, post_edit, post_delete

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<int:post_id>/detail/', post_detail, name='post_detail'),
    path('<int:post_id>/edit/', post_edit, name='post_edit'),
    path('<int:post_id>/delete/', post_delete, name='post_delete'),
    path('posts/api/', PostListAPIView.as_view(), name='api_post_list'),
    path('posts/api/<int:post_id>/', PostRetrieveAPIView.as_view(), name='api_post_detail'),
]