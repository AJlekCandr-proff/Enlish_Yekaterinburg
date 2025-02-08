from typing import Any

from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..models import CustomUserModel


class UserProfileView(TemplateView):
    template_name = 'user/pages/account.html'

    def get_context_data(self, **kwargs) -> dict[str, Any] | str:
        context = super().get_context_data(**kwargs)

        current_user = self.request.user

        if not current_user:
            return reverse_lazy('user:login')

        try:
            user = get_object_or_404(CustomUserModel, email=current_user)

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['user_profile'] = user

        context['title'] = f'Профиль пользователя {user}'

        return context
