from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.utils.text import slugify

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


def article_operation(self, serializer):
    """
        A function that performs a put or create 
        operation on an article
    """
    slug = slugify(serializer.validated_data.get("title"))
    user = self.request.user
    return serializer.save(author=user, slug=slug)

def comment_operation(self, serializer):
    """
        A function that performs a put or create 
        operation on a comment
    """
    author = self.request.user
    article = Article.objects.get(slug=self.kwargs['slug'])
    return serializer.save(author=author, article=article)


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
        #   create an article
        return article_operation(self, serializer)
    

class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        This class defines the update, delete and detail
        behavior of an article api.
    """
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = "slug"

    def get_queryset(self):
        #   get an article using it's slug
        return Article.objects.filter(slug=self.kwargs['slug'])

    def perform_update(self, serializer):
        #   update an article if serializer deems the payload valid
        if serializer.is_valid():
            return article_operation(self, serializer)
        else:
            return Response({'error': serializer.error}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['PATCH',])
@permission_classes((IsAuthenticated,))
@authentication_classes([TokenAuthentication])
def user_preference(request, *args, **kwargs):
    """
        Endpoint to like or dislike an article
    """
    #   check if articl exists
    try:
        article = Article.objects.filter(slug=kwargs['slug'])[0]
    except Article.DoesNotExist:
        return Response({'error: no order record exists yet'}, status=status.HTTP_404_NOT_FOUND)
    
    #   get user reference payload and edit article preference
    preference = request.data['preference']
    if preference == 'like':
        if request.user not in article.likes:
            article.likes.add(request.user)
        else:
            article.likes.remove(request.user)
    else:
        if request.user not in article.dislikes:
            article.dislikes.add(request.user)
        else:
            article.dislikes.remove(request.user)
    return Response({'message': f'preference changed successfully'}, status=status.HTTP_200_OK)


class CommentAPIView(ListCreateAPIView):
    """
        This class defines the create and list
        behavior of comment api.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        #   create a comment
        return comment_operation(self, serializer)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        This class defines the update, delete and detail
        behavior of a comment api.
    """
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        #   get an article using it's slug
        return Comment.objects.filter(id=self.kwargs['id'])

    def perform_update(self, serializer):
        #   create a comment
        if serializer.is_valid():
            comment_operation(self, serializer)
        else:
            return Response({'error': serializer.error}, status=status.HTTP_406_NOT_ACCEPTABLE)
