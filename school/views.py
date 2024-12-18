from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: WSGIRequest) -> HttpResponse:
    """
    Функция представления для главной страницы.

    :param request: Объект класса WSGIRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, '../templates/school/index.html')


def teachers(request: WSGIRequest) -> HttpResponse:
    """
    Функция представления для страницы предподавателей.

    :param request: Объект класса WSGIRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, '../templates/school/teachers.html')


def account(request: WSGIRequest) -> HttpResponse:
    """
    Функция представления для страницы личного кабинета предподавателя или студента.

    :param request: Объект класса WSGIRequest.

    :return: Объект класса HttpResponse.
    """

    return render(request, '../templates/school/account.html')
