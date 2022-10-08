from ast import arg
from django.test import TestCase, Client
from django.urls import reverse
from registrar.models import Course, Student, Register
from .views import index, course, register, add, remove
from django.contrib.auth.models import User

class RegistrarViewTest(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(
            course_code="CN1", 
            course_name="A", 
            semester=1,
            year=2565,
            seat=2,
            status=1
        )

        user1 = User.objects.create_user(username='user1', password='sunday11')
        user1.save()

        self.student1 = Student.objects.create(
            username=user1, 
            first="Loki", 
            last="Laufeyson"
        )

    def test_index_view(self):
        c = Client()
        response=c.get(reverse('rgindex'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/index.html')

    def test_course_view(self):
        c = Client()
        response=c.get(reverse('course', args=[self.course1.id,]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/course.html')

    def test_register_view(self):
        c = Client()
        response=c.get(reverse('register', args=[self.student1.username,]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_add_view(self):
        c = Client()
        response=c.get(reverse('registrar:add',args=[self.student1.username, self.course1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_remove_view(self):
        c = Client()
        response=c.get(reverse('registrar:remove',args=[self.student1.username, self.course1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')