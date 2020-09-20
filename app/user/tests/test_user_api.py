from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_API_URL = reverse('user:create')
CREATE_TOKEN_URL = reverse('user:token')

def create_user(**payload):
    return get_user_model().objects.create_user(**payload)


class TestUserCreate(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpassword',
            'name': 'Test user'
        }

        res = self.client.post(CREATE_USER_API_URL, payload)
        user = get_user_model().objects.get(**res.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_already_exists(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpassword',
            'name': 'Test user'
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_API_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_length(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'test',
            'name': 'Test user'
        }

        res = self.client.post(CREATE_USER_API_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_token_success(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'test',
            'name': 'Test user'
        }
        create_user(**payload)
        res = self.client.post(CREATE_TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK) 
        self.assertIn('token', res.data)
    
    def test_user_not_exist_token_fail(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'test',
            'name': 'Test user'
        }

        res = self.client.post(CREATE_TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST) 
        self.assertNotIn('token', res.data)

    def test_credential_wrong_token_fail(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'test'
        }
        create_user(email=payload['email'], password='testpass')
        res = self.client.post(CREATE_TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST) 
        self.assertNotIn('token', res.data)
