import random

from string import digits

from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.conf import settings

from ..forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm

    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}

    def form_valid(self, form):
        login_code = ''.join(random.choices(digits, k=6))

        user = form.save(commit=False)
        user.code_from_mail = login_code

        send_mail(
            'Подтверждение входа',
            f'Код для входа в аккаунт {login_code}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )

        user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user:registration-confirm', kwargs={'email': self.object.email})
