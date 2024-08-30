"""
URL configuration for ExamApp project.

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

from TestApp.views import *

urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
    path('new-candidate/', candidateRegistrationForm, name='registrationForm'),
    path('login/', loginView, name='login'),
    path('home/', candidateHome, name='home'),
    path('test-paper/', testPaper, name='testPaper'),
    path('calculate-result/', calculateTestResult, name='calculateTest'),
    path('test-history/', testResultHistory, name='testHistory'),
    path('result/', showTestResult, name='result'),
    path('logout/', logoutView, name='logout'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('TestApp/', include('TestApp.urls')),
# ]
