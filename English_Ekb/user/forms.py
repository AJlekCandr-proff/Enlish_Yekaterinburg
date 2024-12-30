from django.forms import PasswordInput, CharField
from django.contrib.auth.forms import AuthenticationForm

from .models import Students


class LoginStudentForm(AuthenticationForm):
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
        fields = ['password']
