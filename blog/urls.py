from django.urls import path
from blog import views

urlpatterns = [
    path('articles/', views.ArticleAPIView.as_view(), name="articles"),
]