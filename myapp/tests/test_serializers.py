import unittest
from django.test import TestCase
from myapp.models import Item
from myapp.serializers import ItemSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User

class ItemSerializerTests(TestCase):
    def setUp(self):
        self.item_attributes = {
            'name': 'Test Item',
            'description': 'Test Description'
        }
        self.serializer_data = {
            'name': 'Test Item',
            'description': 'Test Description'
        }
        self.item = Item.objects.create(**self.item_attributes)
        self.serializer = ItemSerializer(instance=self.item)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name', 'description'])

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.item_attributes['name'])

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.item_attributes['description'])

class UserRegistrationSerializerTests(TestCase):
    def setUp(self):
        self.user_attributes = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        self.serializer_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        self.user = User.objects.create_user(**self.user_attributes)
        self.serializer = UserRegistrationSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'username', 'email'])

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user_attributes['username'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])