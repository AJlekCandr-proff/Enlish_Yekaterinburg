from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, TemplateView
from django.urls import reverse_lazy

from .forms import LoginUserForm
from .models import CustomUser


class LoginCustomView(LoginView):
    authentication_form = LoginUserForm

    template_name = 'user/pages/login.html'
    extra_context = {'title': 'Вход в личный кабинет'}

    def get_success_url(self):
        return reverse_lazy('school:account')


class UserProfileView(TemplateView):
    template_name = 'user/pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            user = get_object_or_404(CustomUser, mail=self.kwargs.get('mail'))

        except CustomUser.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['user_profile'] = user
        context['user_profile'] = user

        context['title'] = f'Профиль пользователя {user}'

        return context


def registration(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для регистрации аккаунта нового студента.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request=request, template_name='school/pages/registration.html')
