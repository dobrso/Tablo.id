from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions, viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

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

@extend_schema_view(
    list=extend_schema(
        summary='Получить посты',
        description='Возвращает посты',
        tags=['Пост'],
    ),
    create=extend_schema(
        summary='Создать новый пост',
        description='Создает новый пост',
        tags=['Пост'],
    ),
    retrieve=extend_schema(
        summary='Получить информацию о посте',
        description='Возвращает детальную информацию о посте по указанному ID.',
        tags=['Пост'],
    ),
    update=extend_schema(
        summary='Полное обновление поста',
        description='Обновляет все поля поста',
        tags=['Пост'],
    ),
    partial_update=extend_schema(
        summary='Частичное обновление поста',
        description='Обновляет отдельные поля поста',
        tags=['Пост'],
    ),
    destroy=extend_schema(
        summary='Удалить пост',
        description='Удаляет пост',
        tags=['Пост'],
    ),
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer