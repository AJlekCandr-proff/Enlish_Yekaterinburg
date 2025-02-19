from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from ..forms import LoginUserForm


class LoginUserView(LoginView):
    authentication_form = LoginUserForm
    template_name = 'user/pages/login.html'
    extra_context = {'title': 'Вход в личный кабинет'}

    email: str | None = None

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user:
            return redirect('user:profile')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: LoginUserForm) -> HttpResponse:
        self.email = form.cleaned_data.get('username')

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('user:login-confirm', kwargs={'email': self.email})
