import unittest
from django.test import TestCase
from myapp.models import Item
from django.contrib.auth.models import User

class ItemModelTests(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name='Test Item', description='Test Description')

    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'Test Description')

    def test_item_str(self):
        self.assertEqual(str(self.item), 'Test Item')

class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')