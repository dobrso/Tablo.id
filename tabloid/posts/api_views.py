from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from drf_spectacular.utils import extend_schema

from .models import Post
from .serializers import PostSerializer, SimplePostSerializer


@extend_schema(
    summary='Список всех постов',
    description='Возвращает список всех доступных постов. Не требует авторизацию.',
    tags=['Пост'],
)
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer

@extend_schema(
    summary='Детальная информация о посте',
    description='Возвращает детальную информацию о посте по его ID. Требует авторизацию.',
    tags=['Пост'],
)
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Post.objects.get(id=self.kwargs['post_id'])