from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

# Create your forms here.

class NewUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': '********'
        }))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': '********'
        }))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Kurobyro',
                'type': 'username'
            }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'name': 'email',
                'placeholder': "example@gmail.com"
            })
        }


class LoginForm(AuthenticationForm):
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'class': 'textbox-auth',
            'placeholder': '********'
        }))
    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {'username': forms.TextInput(attrs={
                    'class': 'textbox-auth',
                    'placeholder': 'Kurobyro',
                    'type': 'username'
                })
        }
