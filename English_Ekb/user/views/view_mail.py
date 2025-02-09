from typing import Any

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from rest_framework_simplejwt.tokens import RefreshToken

from ..forms import ConfirmationCodeForm
from ..models import CustomUserModel


class ConfirmMailView(FormView):
    form_class = ConfirmationCodeForm

    template_name = 'user/pages/mail.html'
    extra_context = {'title': 'Подтверждение почты'}

    def form_valid(self, form: ConfirmationCodeForm) -> HttpResponseRedirect:
        entered_code = form.cleaned_data.get('code')

        user = CustomUserModel.objects.get(email=self.kwargs.get('email'))

        if entered_code == user.code_from_mail:
            refresh_token = RefreshToken.for_user(user)
            refresh_token['email'] = user.email

            access_token = str(refresh_token.access_token)

            response = super().form_valid(form)

            response.set_cookie(
                key='Authorization',
                value=access_token,
                max_age=36000,
            )

            return response

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        try:
            user = get_object_or_404(CustomUserModel, email=self.kwargs.get('email'))

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['title'] = f'Подтверждение почты {user.email}'

        return context

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile')
