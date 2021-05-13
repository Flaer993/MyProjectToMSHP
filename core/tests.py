from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from core.forms import RegisterUserForm, AuthUserForm
from core.views import RegisterUserView, MyprojectLoginView


class RegisterPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('register_page'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), RegisterUserView)
        self.assertEqual(type(self.response.context['form']), RegisterUserForm)


class LoginPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('login_page'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), MyprojectLoginView)
        self.assertEqual(type(self.response.context['form']), AuthUserForm)


class LogoutPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('logout_page'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 302)

    '''def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), LogoutView)
        self.assertEqual(type(self.response.context['form']), AuthUserForm)'''

class CommentPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('logout_page'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 302)





'''
class LoginPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('login_page'))

    def test_index_redirect(self):
        self.assertRedirects(self.response, '')'''