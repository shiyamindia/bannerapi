"""
Test django admin modifications
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

class AdminSiteTests(TestCase):
    """ Admin test for user creations """

    def setUp(self):
        """ Create admin user and normal user """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@admin.com',
            password='testadmin@123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@user.com',
            password='testuesr@123',
            name='Test User',
        )

    def test_users_list(self):
        """ Test the user listed on the page """

        url =reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """ test user edit page is works """

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test the user create page """

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)