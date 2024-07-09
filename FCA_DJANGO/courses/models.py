from django.db import models
from django.utils.text import slugify
class Course(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 650)
    price = models.IntegerField(default = 999)
    students_numbe = models.IntegerField()
    course_hours = models.FloatField()
    instructor_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='courses/images/')
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True )
    
    
    
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    
    
class category(models.Model):
    name = models.CharField( max_length = 50)
    
    def __str__(self):
        return self.name
    
    
    
class enrolling(models.Model):
    name = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, auto_created= True)
    
    def __str__(self):
        return self.name + ' - '  +  self.phone