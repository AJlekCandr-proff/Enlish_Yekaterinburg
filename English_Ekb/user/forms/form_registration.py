from django.forms import PasswordInput, CharField
from django.contrib.auth.forms import UserCreationForm

from ..models.users import CustomUserModel


class LoginUserForm(UserCreationForm):
    password = CharField(
        max_length=15,
        label='password',
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )

    class Meta:
        model = CustomUserModel
        fields = ['password']
