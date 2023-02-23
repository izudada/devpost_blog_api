from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        ArticleAPIView,
                        ArticleDetailAPIView,
                        user_preference,
                        CommentAPIView
                    )


class TestUrls(SimpleTestCase):

    def test_articles_api_resolves(self):
        url = reverse('articles')
        self.assertEquals(resolve(url).func.view_class, ArticleAPIView)

    def test_article_api_resolves(self):
        url = reverse('article', kwargs={'slug': "how-to"})
        self.assertEquals(resolve(url).func.view_class, ArticleDetailAPIView)
    
    def test_preference_api_resolves(self):
        url = reverse('preference', kwargs={'slug': "how-to"})
        self.assertEquals(resolve(url).func, user_preference)

    def test_comments_api_resolves(self):
        url = reverse('comments', kwargs={'slug': "how-to"})
        self.assertEquals(resolve(url).func.view_class, CommentAPIView)