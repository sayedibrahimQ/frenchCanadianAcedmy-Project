from django.contrib import admin
from .models import Course, category, enrolling
# Register your models here.

admin.site.register(Course)
admin.site.register(category)
admin.site.register(enrolling)