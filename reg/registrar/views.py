from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
from .models import Course, Student, Register

def index(request):
    courses = Course.objects.all()
    
    return render(request, 'registrar\\index.html', {
        'courses': courses,
    })

def count(request, course_code):
    course = Course.objects.get(id=course_code)
    register = Register.objects.filter(course=course).all()

    return render(request, 'registrar\\index.html', {
        'course': course,
        'count': len(register),
    })

def course(request, course_code):
    course = Course.objects.get(id=course_code)

    return render(request, 'registrar\\course.html', {
        'course': course,
    })

def register(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(username=user)
    rg = Register.objects.get(student=student)
    return  render(request, 'registrar\\register.html', {
        'rg_course': rg.course.all(),
        "nonrg_course": Course.objects.exclude(rg_course=rg).all(),
    })
    
def remove(request, student_id , rgist):

    rgist.delete()
    return HttpResponseRedirect(reverse('registrar\\course.html'))

def myenroll(request):
    student = Student.objects.get(username=request.user.username)
    enroll = Register.objects.filter(student=student).all()

    return render(request, 'registrar\\course.html', {
        'enroll': enroll,
    })

