from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Course
from .forms import Enroll

def courses_list(request):
    all_courses = Course.objects.all()
    paginator = Paginator(all_courses, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'courses' : page_object
    }
    
    return render(request, 'display_courses.html', context)


def course(request, id):
    global course_details
    course_details = Course.objects.get(id=id)
    context = {
        'course' : course_details,
    }
    return render(request, 'course_details.html', context)


def enroll(request, id):
    course_details = Course.objects.get(id=id)
    if request.method == 'POST':
        form = Enroll(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.course = course_details
            myform.save()
            return render(request, 'succ.html')
    else:
        form = Enroll

    context = {
        'form' : form,
        'course' : course_details,
        }
    return render(request, 'enroll_page.html', context)

def course_id():
    course_details = Course.objects.get(id=id)
