from django.contrib import admin
from django.urls import path
from .views import course, courses_list, enroll

app_name = 'courses'

urlpatterns = [
    path('<str:id>/enroll/', enroll , name = 'enroll'),
    path('<str:id>', course, name = 'course_detail'),
    path('', courses_list),
    
]


