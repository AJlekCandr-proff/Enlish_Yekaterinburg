from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..models import Students, Lessons


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
