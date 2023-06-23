from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Опціонально', label="Імʼя")
    last_name = forms.CharField(max_length=30, required=False, help_text='Опціонально',  label="Прізвище")
    email = forms.EmailField(max_length=254, help_text='Обовʼязково. Повідомте дійсну електронну пошту.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
