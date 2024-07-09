from django.shortcuts import render
from courses.models import Course
# Create your views here.

def home(request):
    courses = Course.objects.all()[:3]
    context = {'courses' : courses}
    return render(request, 'index.html', context)
