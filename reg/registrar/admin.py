from django.contrib import admin
from .models import Course, Student, Register

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first', 'last']
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'semester', 'year', 'seat', 'status']

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Register)