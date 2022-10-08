from django.test import TestCase
from .models import Course, Student, Register
from django.contrib.auth.models import User

# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self):
        course1 = Course.objects.create(
            course_code="CN1", 
            course_name="A", 
            semester=1,
            year=2565,
            seat=1,
            status=1
        )

        user1 = User.objects.create_user(username='user1', password='sunday11', email='sunday@morning.com')
        user1.save()

        student1 = Student.objects.create(
            username=user1, 
            first="Loki", 
            last="Laufeyson"
        )
        
    def test_seat_available(self):
        course = Course.objects.first()
        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        course = Course.objects.first()
        student1 = Student.objects.first()
        register = Register.objects.create(student=student1)

        course.rg_course.add(register)

        self.assertFalse(course.is_seat_available())
