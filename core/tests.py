from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from core.forms import RegisterUserForm
from core.views import RegisterUserView


class RegisterPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('register_page'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), RegisterUserView)
        self.assertEqual(type(self.response.context['form']), RegisterUserForm)


'''
class LoginPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('login_page'))
        
    def test_index_redirect(self):
        self.assertRedirects(self.response, '')'''
