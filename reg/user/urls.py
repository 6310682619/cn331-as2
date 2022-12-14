from django.urls import path

from . import views
from registrar import views as rg_veiws

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registrar', rg_veiws.index, name='registrar'),
]