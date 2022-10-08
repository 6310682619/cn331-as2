from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from registrar.models import Course, Student, Register

# Create your tests here.

class UserViewTest(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(
            course_code="CN1", 
            course_name="A", 
            semester=1,
            year=2565,
            seat=2,
            status=1
        )

        user1 = User.objects.create_user(username='user1', password='sunday11', email='sunday@morning.com')
        user1.save()

        self.student1 = Student.objects.create(
            username=user1, 
            first="Loki", 
            last="Laufeyson"
        )

    def test_user(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})
        response = c.get(reverse('user'))

        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'user/index.html')

    def test_login_view(self):
        c = Client()
        response = c.get(reverse('login'))
        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_in(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})
        response = c.get(reverse('index'))

        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'user/index.html')

    def test_logged_out(self):
        c = Client()
        response = c.get(reverse('logout'))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['message'] == 'Logged out')
        # Check template
        self.assertTemplateUsed(response, 'user/login.html')

    def test_not_user_login(self):
        c = Client()
        response = c.post(reverse('login'),
               {'username': 'user3', 
               'password': 'tuesday3'})

        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)