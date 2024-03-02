from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username='testuser', email='test@example.com')

    def test_user_username(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'testuser')

    def test_user_email(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.email, 'test@example.com')
