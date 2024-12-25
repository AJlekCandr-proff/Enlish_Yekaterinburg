from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models.lessons import Students, Lessons


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для главной страницы.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, 'school/pages/home.html')


def teachers(request: HttpRequest) -> HttpResponse:
    """ Функция представления для страницы преподавателей.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, 'school/pages/teachers.html')


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
