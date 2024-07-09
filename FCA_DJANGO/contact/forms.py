from django.forms import ModelForm, Textarea, TextInput, EmailInput, HiddenInput
from .models import contact

class contactUs(ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class' : 'form-control', 'placeholder' : "FIRST NAME" , 'id' : "name"}),
            'email' : EmailInput(attrs={'class': 'form-control',  'placeholder' : "E-MAIL" , 'id' : "email"}),
            'phone_number' : TextInput(attrs={'class': 'form-control',  'placeholder' : "PHONE NUMBER" ,  'id' : "phone"}),
            'subject' : TextInput(attrs={'class': 'form-control',  'placeholder' : "SUBJECT", 'id' : "subject"}),
            'message' : Textarea(attrs={'class': 'form-control',  'placeholder' : "MESSAGE" , 'id' : "message",'style' : "height: 150px"}),
        }
        labels = {
            'name' : 'YOUR NAME',
            'email' : 'YOUR EMAIL',
            'phone_number' : 'PHONE NUMBER',
            'subject' : 'SUBJECT',
            'message' : 'MESSAGE',
        }   