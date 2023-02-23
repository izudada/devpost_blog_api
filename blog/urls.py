from django.urls import path
from .views import (
                    ArticleAPIView,
                    ArticleDetailAPIView,
                    user_preference
                )

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name="articles"),
    path('articles/<slug:slug>/', ArticleDetailAPIView.as_view(), name="article"),
    path('articles/<slug:slug>/preference/', user_preference, name="preference"),
]