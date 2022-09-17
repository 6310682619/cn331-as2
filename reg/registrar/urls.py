from django.urls import path

from . import views

app_name = 'registrar'

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('register/<int:course_code>', views.register, name='register'),
    path('remove/', views.remove, name='remove'),
]