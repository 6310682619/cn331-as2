from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Course, Student, Register

def index(request):
    student = Student.objects.filter(username=request.user.username).first()
    regists = Register.objects.filter(student=student).all()
    courses = Course.objects.exclude(pk__in=regists).all()
    courses = Course.objects.all()
    
    return render(request, 'registrar/index.html', {
        'courses': courses,
    })

def count(request, course_code):
    course = Course.objects.get(id=course_code)
    register = Register.objects.filter(course=course).all()

    return render(request, 'registrar/index.html', {
        'course': course,
        'count': len(register),
    })

def course(request, course_code):
    course = Course.objects.get(id=course_code)

    return render(request, 'registrar/course.html', {
        'course': course,
    })

def register(request, course_code):
    student = Student.objects.get(pk=request.user.id)
    course = Course.objects.get(pk=course_code)

    check = Register.objects.filter(student=student, course=course).first()
    if not check:
        return myenroll(request)

def remove(request, course_code):
    student = Student.objects.get(username=request.user.username)
    course = Course.objects.get(pk=course_code)
    regist = Register.objects.get(student=student, course=course)

    if regist:
        unregist = regist.delete()
        if unregist:
            return HttpResponseRedirect(reverse('registrar:index'))

def myenroll(request):
    student = Student.objects.get(username=request.user.username)
    enroll = Register.objects.filter(student=student).all()

    return render(request, 'registrar/course.html', {
        'enroll': enroll,
    })
