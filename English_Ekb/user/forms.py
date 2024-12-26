from django.forms import EmailField, PasswordInput, TextInput, CharField
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User


class LoginStudentForm(AuthenticationForm):
    mail = EmailField(
        label='Email',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    password = CharField(
        max_length=128,
        label='Пароль',
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )

    class Meta:
        model = User
        fields = ['mail', 'password']
