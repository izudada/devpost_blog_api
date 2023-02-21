from django.test import SimpleTestCase
from django.urls import resolve, reverse

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        register,
                        login_user,
                        user_logout
                    )


class TestUrls(SimpleTestCase):

    def test_register_api_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_api_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_api_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, user_logout)