from jwt import decode

from django.conf import settings
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..models import CustomUserModel


class UserProfileView(TemplateView):
    template_name = 'user/pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        jwt_token = self.request.COOKIES.get('Authorization')

        decoded_token = decode(jwt=jwt_token, algorithms=['HS256'], key=settings.SECRET_KEY)

        if not decoded_token:
            return reverse_lazy('user:login')

        try:
            user = get_object_or_404(CustomUserModel, email=decoded_token.get('email'))

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['user_profile'] = user

        context['title'] = f'Профиль пользователя {user}'

        return context
