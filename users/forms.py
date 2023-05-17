from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@gmail.com',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '******',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
