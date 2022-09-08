"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """ test models """

    def test_create_user_with_email_successful(self):
        """ test for creating user using email """

        email = 'tesst@test.com'
        password = 'testpass@123'
        user = get_user_model().objects.create_user (
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, user.check_password(password))
