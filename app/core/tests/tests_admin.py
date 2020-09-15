from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_super_user(
            email='admin@gmail.com',
            password='Pass1234'
        )

        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='pass1234',
            name='Test User'
        )

    def test_contains_user(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
