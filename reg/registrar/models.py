from django.db import models

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

class Student(models.Model):
    username = models.CharField(max_length=20)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f'{ self.first } { self.last } ({ self.username })'

class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return f"{ self.student } { self.course }"