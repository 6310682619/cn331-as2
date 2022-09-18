from django.urls import path

from . import views
from user import views as u_views

urlpatterns = [
    path('', views.index, name='rgindex'),
    path('<int:course_code>/course', views.course, name='course'),
    path('<username>/register', views.register, name='register'),
    path('<int:student_id>/remove', views.remove, name='remove'),
    path('user', u_views.user, name='user'),
    path('logout', u_views.logout_view, name='logout'),
]