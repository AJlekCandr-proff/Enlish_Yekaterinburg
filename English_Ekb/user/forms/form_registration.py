from django.forms import EmailInput, EmailField
from django.contrib.auth.forms import BaseUserCreationForm

from ..models.users import CustomUserModel


class RegistrationUserForm(BaseUserCreationForm):
    email = EmailField(
         label='email',
         widget=EmailInput(attrs={
             'class': 'form-control',
             'placeholder': 'Электронная почта'
         })
    )

    class Meta:
        model = CustomUserModel
        fields = ['email']
