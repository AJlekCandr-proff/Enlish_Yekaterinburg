from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """
    Функция представления для главной страницы.

    :param request:

    :return: Объект класса HttpResponse.
    """

    return render(request, 'school/index.html')
