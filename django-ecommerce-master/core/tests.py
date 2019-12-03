from django.test import TestCase
from core.models import Item
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
          resp = c.get('/checkout')
          self.assertEqual(resp.status_code, 200)
          resp = c.get('/ordersummary')
          self.assertEqual(resp.status_code, 200)
class DatabaseTestCase(TestCase):
    def testItem(self):
        # Insert into core_item(id,title,price,label,slug,description,image,category) values (3, "",8,'S','ATTWN','One of the most famous and beloved mysteries from The Queen of Suspense—Agatha Christie—now a Lifetime TV movie.','ATTWN.jpg','fiction');
        Item.objects.create(id=1, title ="test",price=30,label="S",slug="test",description="lalalla",image="demp.jpg",category="fiction")
        user = Item.objects.get(id=1)
