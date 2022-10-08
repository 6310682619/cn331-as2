from django.test import TestCase
from .models import Course, Student, Register
from django.contrib.auth.models import User

# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(
            course_code="CN1", 
            course_name="A", 
            semester=1,
            year=2565,
            seat=1,
            status=1
        )

        user1 = User.objects.create_user(username='user1', password='sunday11')
        user1.save()
        user2 = User.objects.create_user(username='user2', password='monday22')
        user2.save()

        self.student1 = Student.objects.create(
            username=user1, 
            first="Loki", 
            last="Laufeyson"
        )

        self.student2 = Student.objects.create(
            username=user2, 
            first="Tony", 
            last="Stark"
        )
        
    def test_seat_available(self):
        course = Course.objects.first()
        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        course = Course.objects.first()
        student1 = Student.objects.first()

        course.rg_course.add(student1)

        self.assertFalse(course.is_seat_available())
