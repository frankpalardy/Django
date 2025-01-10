# python
from django.test import TestCase
from myapp.forms import ItemForm, UserRegistrationForm

class ItemFormTests(TestCase):
    def test_item_form_valid(self):
        form_data = {'name': 'Test Item', 'description': 'Test Description'}
        form = ItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_item_form_invalid(self):
        form_data = {'name': '', 'description': 'Test Description'}
        form = ItemForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserRegistrationFormTests(TestCase):
    def test_user_registration_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'testuser@example.com'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'differentpassword',
            'email': 'testuser@example.com'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())