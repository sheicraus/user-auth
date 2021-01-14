from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    date = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date']
