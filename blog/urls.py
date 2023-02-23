from django.urls import path
from .views import (
                    ArticleAPIView,
                    ArticleDetailAPIView,
                    user_preference,
                    CommentAPIView,
                    CommentDetailAPIView
                )

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name="articles"),
    path('articles/<slug:slug>/', ArticleDetailAPIView.as_view(), name="article"),
    path('articles/<slug:slug>/preference/', user_preference, name="preference"),
    path('articles/<slug:slug>/comments/', CommentAPIView.as_view(), name="comments"),
    path('articles/<slug:slug>/comments/<int:id>/', CommentDetailAPIView.as_view(), name="comment"),
]