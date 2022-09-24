from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
from .models import Course, Student, Register

def index(request):
    courses = Course.objects.all()
    
    return render(request, 'registrar/index.html', {
        'courses': courses,
    })

def course(request, course_code):
    course = Course.objects.get(id=course_code)

    return render(request, 'registrar/course.html', {
        'course': course,
    })

def register(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(username=user)
    rg = Register.objects.get(student=student)
    return  render(request, 'registrar/register.html', {
        'rg_course': rg.course.all(),
        "nonrg_course": Course.objects.exclude(rg_course=rg).all(),
    })

def add(request, username, course_id):
    user = User.objects.get(username=username)
    student = Student.objects.get(username=user)
    rg = Register.objects.get(student=student)
    course = Course.objects.get(id=course_id)
    rg.course.add(course)
    course.seat -= 1
    course.save()
    return  render(request, 'registrar/register.html', {
        'rg_course': rg.course.all(),
        "nonrg_course": Course.objects.exclude(rg_course=rg).all(),
    })

def remove(request, username, course_id):
    user = User.objects.get(username=username)
    student = Student.objects.get(username=user)
    rg = Register.objects.get(student=student)
    cancle_c = rg.course.get(id=course_id)
    cancle_c.delete()
    cancle_c.seat += 1
    cancle_c.save()
    return HttpResponseRedirect(reverse('register', args=(username,)))
