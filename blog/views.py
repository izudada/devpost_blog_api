from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.utils.text import slugify

from .serializers import ArticleSerializer
from .models import Article


class ArticleAPIView(ListCreateAPIView):
    """
        This class defines the create and list
        behavior of article api.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'author__first_name', 'author__last_name', 'body')

    def perform_create(self, serializer):
        slug = slugify(serializer.validated_data.get("title"))
        user = self.request.user
        return serializer.save(author=user, slug=slug)