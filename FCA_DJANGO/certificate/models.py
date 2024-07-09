from django.db import models
from pdf2image import convert_from_path
# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=50)
    certificate_code = models.CharField(max_length=50)
    national_identity = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    certificate = models.FileField(upload_to="certificates/", verbose_name = 'Certificate')
    cimg = models.ImageField(upload_to="certificates/images/", verbose_name = 'Certificate Image')
    
    def __str__(self):
        return self.name + " - " + self.certificate_code