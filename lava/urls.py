from  django.urls import path
from .import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('dashboard/', views.dashboard, name='dashboard'),


]