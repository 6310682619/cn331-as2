from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Course, Student, Register

def index(request):
    student = Student.objects.filter(pk=request.user.id).first()
    regists = Register.objects.filter(student=student).all()
    courses = Course.objects.exclude(pk__in=regists).all()
    courses = Course.objects.all()

    return render(request, 'registrar/index.html', {
        'courses': courses,
    })

def course(request, course_code):
    student = Student.objects.filter(username=request.user.username).first()
    course = Course.objects.get(id=course_code)
    register = Register.objects.filter(course=course).all()
    enrolled = Register.objects.filter(student=student, course=course).first()

    return render(request, 'registrar/index.html', {
        'course': course,
        'count': len(register),
        'enrolled': enrolled
    })

def register(request, course_code):
    student = Student.objects.get(pk=request.user.id)
    course = Course.objects.get(pk=course_code)

    check = Register.objects.filter(student=student, course=course).first()
    if not check:
        regist = Register.objects.create(student=student, courset=course)

        return HttpResponseRedirect(reverse('registrar:index'))

def remove(request, course_code):
    student = Student.objects.get(username=request.user.username)
    course = Course.objects.get(pk=course_code)
    regist = Register.objects.get(student=student, course=course)

    if regist:
        unregist = regist.delete()
        if unregist:
            return HttpResponseRedirect(reverse('registrar:course'))

#def myenroll(request):
   # student = Student.objects.get(username=request.user.username)
   # enroll = Register.objects.filter(student=student).all()

   # return render(request, 'registrar/myenroll.html', {
   #     'enroll': enroll,
   # })
