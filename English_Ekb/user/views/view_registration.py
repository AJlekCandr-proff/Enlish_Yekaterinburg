from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.conf import settings

from ..forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm

    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}

    def form_valid(self, form):
        user = form.save()

        send_mail(
            'Тестовое письмо',
            'Это тестовое сообщение.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user:registration-confirm')