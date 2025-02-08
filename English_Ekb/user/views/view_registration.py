import random

from string import digits

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.conf import settings
from django.shortcuts import redirect

from ..forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm

    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user:
            return redirect('user:profile')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form) -> HttpResponseRedirect:
        login_code = ''.join(random.choices(digits, k=6))

        user = form.save(commit=False)
        user.code_from_mail = login_code

        user.save()

        send_mail(
            'Подтверждение входа',
            f'Код для входа в аккаунт {login_code}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('user:registration-confirm', kwargs={'email': self.object.email})
