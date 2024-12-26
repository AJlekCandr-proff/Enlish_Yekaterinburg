from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forms import LoginStudentForm
from .models import Students, Lessons


class LoginCustomView(LoginView):
    authentication_form = LoginForm
    template_name = 'school/login.html'
    extra_context = {'title': 'Вход в личный кабинет'}

    def get_success_url(self):
        return reverse_lazy('user:account')


def account(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для страницы личного кабинета преподавателя или студента.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    user_profile = Students.objects.first()

    if user_profile:
        user_lessons = Lessons.objects.filter(pupils__first_name=user_profile.first_name)
    else:
        user_lessons = []

    return render(
        request=request,
        template_name='school/pages/account.html',
        context={'user_profile': user_profile, 'user_lessons': user_lessons}
    )


def login(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для входа в личный кабинет студента или предподавателя.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request=request, template_name='school/pages/login.html')


def registration(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для регистрации аккаунта нового студента.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request=request, template_name='school/pages/registration.html')
