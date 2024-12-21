from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from .models.lessons import Students


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для главной страницы.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, '../templates/school/pages/home.html')


def teachers(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для страницы предподавателей.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, '../templates/school/pages/teachers.html')


def account(request: HttpRequest) -> HttpResponse:
    """
    Функция представления для страницы личного кабинета предподавателя или студента.

    :param request: Объект класса HttpRequest.

    :return: Объект класса HttpResponse.
    """

    user_profile = get_object_or_404(Students)

    return render(request, '../templates/school/pages/account.html', {'user_profile': user_profile})
