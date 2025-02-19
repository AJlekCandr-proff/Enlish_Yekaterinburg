from typing import Any

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from ..models import CustomUserModel


class UserProfileView(TemplateView):
    template_name = 'user/pages/account.html'
    user: CustomUserModel | None = None

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        current_user = self.request.user

        user = CustomUserModel.objects.filter(email=current_user).first()

        if user is None:
            return redirect('user:login')

        self.user = user

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any] | str:
        context = super().get_context_data(**kwargs)

        context['user_profile'] = self.user

        context['title'] = f'Профиль пользователя {self.user.email}'

        return context
