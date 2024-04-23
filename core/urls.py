# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('student_info/', views.student_info, name='student_info'),
    path('success/', views.success, name='success'),
]
