from django.core import validators
from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password','groupe']
        widget = {
            'name ': forms.TextInput(attrs={'class':'form-controle'}),
            'password ': forms.PasswordInput(attrs={'class':'form-controle'}),
            'groupe ': forms.NumberInput(attrs={'class':'form-controle'}),
        }