from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
