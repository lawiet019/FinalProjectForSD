from django.test import TestCase
from core.models import UserProfile
from django.test.client import Client
# Create your tests here.
class ConnectTestCase(TestCase):
      def test_homepage(self):
        c = Client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)
      def test_fictioncategory(self):
        c = Client()
        resp = c.get('/fiction')
        self.assertEqual(resp.status_code, 200)
      def test_nonfictioncategory(self):
        c = Client()
        resp = c.get('/non-fiction')
        self.assertEqual(resp.status_code, 200)
      def test_mangacategory(self):
        c = Client()
        resp = c.get('/manga')
        self.assertEqual(resp.status_code, 200)
class LoginTestCase(TestCase):
      def test_login(self):
          c = Client()
          c.login(username='test', password='abC123456')
