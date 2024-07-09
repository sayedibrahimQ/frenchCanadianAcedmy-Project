from django.forms import ModelForm, TextInput, EmailInput, Select, NumberInput
from .models import enrolling

class Enroll(ModelForm):
    class Meta:
        model = enrolling
        fields = ['name', 'phone', 'email', 'address', 'age']
        widgets = {
            'name': TextInput(attrs={'class' : 'form-control', 'placeholder' : "FIRST NAME" , 'id' : "name" , 'style' : 'width: 100%; height:35px;'}),
            'phone' : TextInput(attrs={'class': 'form-control',  'placeholder' : "PHONE NUMBER" ,  'id' : "" , 'style' : 'width: 100%;height:35px;'}),
            'email' : EmailInput(attrs={'class': 'form-control',  'placeholder' : "E-MAIL" , 'id' : "email" , 'style' : 'width: 100%;height:35px;'}),
            'address' : TextInput(attrs={'class': 'form-control',  'placeholder' : "SUBJECT", 'id' : "subject" , 'style' : 'width: 100%;height:35px;'}),
            'age' : NumberInput(attrs={'class': 'form-control',  'placeholder' : "Your Age", 'id' : "age" , 'style' : 'width: 100%;height:35px;'}),
        }