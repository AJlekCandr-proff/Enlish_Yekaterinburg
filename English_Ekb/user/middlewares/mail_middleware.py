import re

from random import choices

from string import digits

from typing import Callable

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import CustomUserModel


class EmailMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self._get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        path = request.path

        if re.match(r'^.+/(login/|registration/)[\w.-]+@[\w.-]+\.\w+', path) and request.method == 'GET':
            if 'login/' in path:
                email = request.path.split('login/')[1]

            elif 'registration/' in path:
                email = request.path.split('registration/')[1]

            if re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
                login_code = ''.join(choices(digits, k=6))
                user = get_object_or_404(CustomUserModel, email=email)

                user.code_from_mail = login_code

                user.save()

                send_mail(
                    'Подтверждение входа',
                    f'Код для входа в аккаунт {user.code_from_mail}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email]
                )

        return self._get_response(request)
