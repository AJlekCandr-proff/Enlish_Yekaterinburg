from django.forms import EmailField, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginStudentForm(AuthenticationForm):
    mail = EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш Email'
        })
    )

    password = CharField(
        max_length=128,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )

    class Meta:
        model = User
        fields = ['mail', 'password']
