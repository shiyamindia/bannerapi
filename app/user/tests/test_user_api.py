"""
Test for the user API
"""

from genericpath import exists
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """ Test the public features foe user Api """

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """ test create the user is created successfully """

        payload = {
            'email' : 'test@test1.com',
            'password' : 'test@test123',
            'name' : 'testapi',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email =payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_check_user_email_exists(self):
        """ Check user email is already exist in DB """

        payload = {
            'email' : 'test@test1.com',
            'password' : 'test@test123',
            'name' : 'testapi',
        }

        create_user(**payload)
        res =  self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_is_too_short(self):
        """ test password is too short error """

        payload = {
            'email' : 'test@test13.com',
            'password' : 'te',
            'name' : 'testpasscheck',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email= payload['email']
        ).exists()

        self.assertFalse(user_exists)
