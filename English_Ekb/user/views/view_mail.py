from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..models import CustomUserModel


class ConfirmMailView(TemplateView):
    template_name = 'user/pages/mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            user = get_object_or_404(CustomUserModel, email=kwargs.get('email'))

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['title'] = f'Подтверждение почты {user.email}'

        return context
