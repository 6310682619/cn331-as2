from django.db import models
from django.contrib.auth.models import User

# Create your models here.
       
class Course(models.Model):
    course_code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()

    class Status(models.IntegerChoices):
        Available = 1
        Unavailable = 0
    status = models.IntegerField(choices=Status.choices)

    def __str__(self):
        return f"{ self.course_code } { self.course_name } { self.semester } { self.year } { self.seat } { self.status }"

    def is_seat_available(self):
        return self.rg_course.count() < self.seat

class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student", null=True)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f'{ self.first } { self.last } ({ self.username })'

class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="rg_student")
    course = models.ManyToManyField(Course, blank=True, related_name="rg_course")

    def __str__(self):
        return f"{ self.student } { self.course }"