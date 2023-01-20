from django.core import validators
from django import forms
from .models import User


class UserRegistration(forms.Form):
    class Meta:
        model1 = User
        fields = ['name','password','groupe']
        widget = {
            'name ': forms.TextInput(attrs={'class':'form-controle'}),
            'password ': forms.PasswordInput(attrs={'class':'form-controle'}),
            'name ': forms.NumberInput(attrs={'class':'form-controle'}),
        }