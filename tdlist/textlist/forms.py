from django import forms
from .models import *

class addnoteform(forms.Form):
    title_note = forms.CharField(max_length=255)
    time_note = models.TimeField()
    text_note = forms.CharField(max_length=255)
    telegram_send = models.BooleanField()
    day_of_week = models.SmallIntegerField()
    
class AddCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name_cust', 'mail_cust', 'password_cust']
        
        widgets = {
            "name_cust": forms.TextInput(attrs={
                'class': 'textbox-auth',
                'placeholder': "Kurobyro",
                'type':"username"
            }),
            "mail_cust": forms.TextInput(attrs={
                'class': 'textbox-auth',
                'type': 'email',
                'name': 'username',
                'placeholder': "Hitler@jew.hot"
            }),
            "password_cust": forms.TextInput(attrs={
                'class': 'textbox-auth', 
                'placeholder': '*********',
                'type': 'password'
            })
        }