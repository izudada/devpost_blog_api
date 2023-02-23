from django.urls import path
from .views import (
                    ArticleAPIView,
                    ArticleDetailAPIView
                )

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name="articles"),
    path('articles/<slug:slug>/', ArticleDetailAPIView.as_view(), name="article"),
]