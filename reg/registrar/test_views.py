from ast import arg
from django.test import TestCase, Client
from django.urls import reverse
from registrar.models import Course, Student, Register
from .views import index, course, register, add, remove
from django.contrib.auth.models import User

class RegistrarViewTest(TestCase):
    def setUp(self):
        course1 = Course.objects.create(
            course_code="CN1", 
            course_name="A", 
            semester=1,
            year=2565,
            seat=2,
            status=1
        )

        user1 = User.objects.create_user(username='user1', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='user2', password='monday22', email='monday@morning.com')

        student1 = Student.objects.create(
            username=user1, 
            first="Loki", 
            last="Laufeyson"
        )

        student2 = Student.objects.create(
            username=user2, 
            first="Tony", 
            last="Stark"
        )

        rg = Register.objects.create(student=student1)
        rg2 = Register.objects.create(student=student2)
        course = Course.objects.first()
        course.rg_course.add(rg)

    def test_index_view(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})
        response=c.get(reverse('rgindex'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/index.html')

    def test_course_view(self):
        c = Client()
        course1 = Course.objects.first()
        response=c.get(reverse('course', args=[course1.id,]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/course.html')

    def test_register_view(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})
        student1 = Student.objects.first()
        response=c.get(reverse('register', args=[student1.username,]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_add_view(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})
        student1 = Student.objects.first()
        course1 = Course.objects.first()
        response=c.get(reverse('add',args=[student1.username, course1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_remove_view(self):
        c = Client()
        c.post(reverse('login'),
               {'username': 'user1', 
               'password': 'sunday11'})

        student1 = Student.objects.first()
        course1 = Course.objects.first()
        response=c.get(reverse('remove',args=[student1.username, course1.id]))
        # Check response
        self.assertEqual(response.status_code, 302)