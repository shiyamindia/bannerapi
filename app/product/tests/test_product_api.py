"""
Test for product Api
"""

from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product

from product.serializers import (
    ProductSerializer,
    ProductDetailSerializer,
)

PRODUCT_URL = reverse('products:product-list')

def detail_url(product_id):
    """ Craete and return the product detail URL """
    return reverse('products:product-detail', args=[product_id])

def create_product(user, **params):
    """ Create and retuen the sample product """
    defaults = {
        "name": "testname",
        "sku": "test00011",
        "price": Decimal('100.35'),
        "description": "test description",
        "is_giftcard":True
    }

    defaults.update(params)

    product = Product.objects.create(user=user, **defaults)
    return product

class PublicProductAPITests(TestCase):
    """ Test unauthencated API request """

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ test auth is required to call the api """

        res = self.client.get(PRODUCT_URL)

        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateProductApiTests(TestCase):
    """ Test for authenticated API request """

    def setUp(self):
        self.client= APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_product_list(self):
        """ Test for getting product list """

        create_product(user=self.user)
        create_product(user=self.user)

        result = self.client.get(PRODUCT_URL)

        product = Product.objects.all().order_by('-id')
        serializer= ProductSerializer(product, many=True)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data, serializer.data)

    def test_product_list_limited_to_user(self):
        """ Test for getting product list for limited base on user """
        other_user = get_user_model().objects.create_user(
            'other@example.com',
            'otherpass'
        )
        create_product(user=other_user)
        create_product(user=self.user)

        result = self.client.get(PRODUCT_URL)

        product = Product.objects.filter(user=self.user)
        serializer= ProductSerializer(product, many=True)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data, serializer.data)

    def test_get_product_details(self):
        """ test for getting product details """

        product= create_product(self.user)

        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductDetailSerializer(product)
        self.assertEquals(res.data, serializer.data)

    def test_create_product(self):
        """ Test for create the product """

        payload = {
            'name' : 'testname',
            'sku' : 'testsku1',
            'price': Decimal('35.50'),
        }

        res = self.client.post(PRODUCT_URL, payload)

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get(id=res.data['id'])
        for key, value in payload.items():
            self.assertEquals(getattr(product, key), value)
        self.assertEquals(product.user, self.user)