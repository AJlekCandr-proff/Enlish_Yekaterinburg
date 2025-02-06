from jwt import decode

from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..models import CustomUserModel
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        jwt_token = self.request.headers.get('Authorization')

        if jwt_token and jwt_token.startswith('Bearer '):
            jwt_token = jwt_token.split(' ')[1]

        print(jwt_token)

        decoded_token = decode(jwt_token, algorithms=['HS256'])

        if not decoded_token:
            return reverse_lazy('user:login')

        try:
            user = get_object_or_404(CustomUserModel, email=self.request.user.email)

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['user_profile'] = user

        context['title'] = f'Профиль пользователя {user}'

        return context
