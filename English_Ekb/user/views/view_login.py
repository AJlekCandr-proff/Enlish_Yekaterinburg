from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from ..forms.form_login import LoginUserForm


class LoginUserView(LoginView):
    authentication_form = LoginUserForm

    template_name = 'user/pages/login.html'
    extra_context = {'title': 'Вход в личный кабинет'}

    def get_success_url(self):
        return reverse_lazy('user:profile')
