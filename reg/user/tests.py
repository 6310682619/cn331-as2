from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class UserViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='sunday')
        user1.save()

    def test_logged_in(self):
        c = Client()
        login = c.login(username='user1', password='sunday')
        response = c.get(reverse('index'))

        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_out(self):
        c = Client()
        response = c.get(reverse('logout'))

        # Check response
        self.assertEqual(response.status_code, 200)