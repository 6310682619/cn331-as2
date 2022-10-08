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
        response = c.post(reverse('user:login'),
               {'username': 'user1', 
               'password': 'sunday11'})

        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_out(self):
        c = Client()
        response = c.get(reverse('logout'))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['message'] == 'Logged out')

    def test_not_user_login(self):
        c = Client()
        response = c.post(reverse('user:login'),
               {'username': 'user3', 
               'password': 'tuesday3'})

        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('user:login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('user:index'))
        self.assertEqual(response.status_code, 302)