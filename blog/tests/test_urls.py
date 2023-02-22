from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        ArticleAPIView
                    )


class TestUrls(SimpleTestCase):

    def test_articles_api_resolves(self):
        url = reverse('articles')
        self.assertEquals(resolve(url).func.view_class, ArticleAPIView)