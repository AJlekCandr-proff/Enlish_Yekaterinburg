from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from ..forms import LoginUserForm


class LoginUserView(LoginView):
    authentication_form = LoginUserForm

    template_name = 'user/pages/login.html'
    extra_context = {'title': 'Вход в личный кабинет'}

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user:
            return redirect('user:profile')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse('user:login-confirm', kwargs={'email': self.object.email})
