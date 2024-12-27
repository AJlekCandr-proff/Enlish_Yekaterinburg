from django.forms import EmailField, PasswordInput, TextInput, CharField, EmailInput
from django.contrib.auth.forms import AuthenticationForm

from .models.students import Students


class LoginStudentForm(AuthenticationForm):
    mail = EmailField(
        label='mail',
        widget=EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    password = CharField(
        max_length=15,
        label='password',
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )

    class Meta:
        model = Students
        fields = ['mail', 'password']
