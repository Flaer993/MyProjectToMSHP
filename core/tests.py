from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from core.forms import RegisterUserForm, AuthUserForm
from core.views import *


class HomePageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('home'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), HomeListView)


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


class FAQPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('faq'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), FAQ)


class ForumPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('forum'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), ForumListView)


class InstrPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('start_inst'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), instr)


class AsusPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('asus'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), ASUS)


class TpLinkPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('tp-link'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), tplink)


class XiaomiPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('xiaomi'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), xiaomi)


class MgtsPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('mgts'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), mgts)


class RosteleckomPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('rosteleckom'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), rostelecom)


class NetisPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('netis'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), netis)


class KeeneticPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('keenetic'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), keenetic)


class HyaweiPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('hyawei'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), hyawei)


class MickrotikPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('mickrotik'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(type(self.response.context['view']), micro)


'''
class LoginPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('login_page'))

    def test_index_redirect(self):
        self.assertRedirects(self.response, '')'''
