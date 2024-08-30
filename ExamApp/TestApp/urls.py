from django.urls import path
from TestApp.views import *
app_name = "TestApp"

urlpatterns = [
    path('/', welcome),
    path('new-candidate/', candidateRegistration, name='registration'),
    path('store-candidate/', candidateRegistration),
    path('login/', loginView, name='login'),
    path('home/', candidateHome),
    path('test-paper/', testPaper),
    path('calculate-result/', calculateTestResult),
    path('test-history/', showTestResult),
    path('logout/', logoutView),
]