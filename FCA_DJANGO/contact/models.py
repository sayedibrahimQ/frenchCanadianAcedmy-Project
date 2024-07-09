from django.db import models

# Create your models here.

class  contact(models.Model):
    name = models.CharField(max_length=100)
    
    email = models.EmailField(blank=False, null=False)
    
    phone_number = models.CharField(max_length=15) 
    
    subject = models.CharField(max_length=100)
    
    message = models.TextField((""), max_length = 1000)
    
    
    def __str__(self):
        title = f'{self.name} \t {self.email}'
        return title