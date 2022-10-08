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

        self.kwargs={'username':self.student1.username,
        'course_id':self.course1.id}

    def test_index_view(self):
        c = Client()
        response=c.get(reverse('rgindex'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/index.html')

    def test_course_view(self):
        c = Client()
        response=c.get(reverse('course', args=(self.course1.id,)))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/course.html')

    def test_register_view(self):
        c = Client()
        response=c.get(reverse('register', args=(self.student1.username,)))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_add_view(self):
        c = Client()
        response=c.get(reverse('add', **self.kwargs))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

    def test_remove_view(self):
        c = Client()
        response=c.get(reverse('remove', **self.kwargs))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'registrar/register.html')

#args=(self.student1.username,), args2=(self.course1.id,)