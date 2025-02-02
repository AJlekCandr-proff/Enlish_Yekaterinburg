from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm

    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}

    def get_success_url(self):
        return reverse_lazy('user:registration-confirm')
