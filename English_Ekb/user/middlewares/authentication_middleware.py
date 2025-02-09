from typing import Callable

import jwt

from django.conf import settings
from django.http import HttpRequest, HttpResponse


class AuthenticationMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self._get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if '/user' in request.path:
            jwt_token = request.COOKIES.get('Authorization')

            if jwt_token:
                try:
                    decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])

                    request.user = decoded_token.get('email')

                except jwt.exceptions.ExpiredSignatureError:
                    request.user = None

            else:
                request.user = None

        return self._get_response(request)
