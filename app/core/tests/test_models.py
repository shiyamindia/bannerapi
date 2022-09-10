"""
Tests for models
"""
from decimal import Decimal
import decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

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

    def test_create_superuser(self):
        """ test creat super user """
        user = get_user_model().objects.create_superuser(
            'testadmin@example.com',
            'test@1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_product(self):
        """ test for creating product successfully """

        user = get_user_model().objects.create_user(
            'testproduct@example.com',
            'testproduct'
        )

        product = models.Product.objects.create(
            user=user,
            name='testproduct1',
            sku='test00001',
            price= Decimal('25.60'),
            description='test product description',
            is_giftcard=True,
        )

        self.assertEquals(str(product), product.name)

