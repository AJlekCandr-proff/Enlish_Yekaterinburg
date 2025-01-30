from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user/pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            user = get_object_or_404(CustomUser, email=self.request.user)

        except CustomUser.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['user_profile'] = user

        context['title'] = f'Профиль пользователя {user}'

        return context
