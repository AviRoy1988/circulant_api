from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):

    def test_user_created_with_email_is_successful(self):
        email = 'testemail@gmail.com'
        password = 'pwd1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'testuser@GMAIL.COM'

        user = get_user_model().objects.create_user(
            email=email,
            password='123456'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, '1234'
            )

    def test_create_new_super_user_success(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
