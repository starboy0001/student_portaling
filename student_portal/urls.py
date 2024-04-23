"""
URL configuration for student_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views import student_info
from lava.views import dashboard



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_info, name='home'),  # Define the root URL pattern
    path('signup/', include('core.urls')),  # Include the core app's URLs
    path('lava/', include('lava.urls')),
   


]