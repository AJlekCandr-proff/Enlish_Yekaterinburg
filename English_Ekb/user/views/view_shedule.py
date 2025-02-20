from typing import Any

from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from ..models import CustomUserModel


class ScheduleView(TemplateView):
    template_name = 'user/pages/schedule.html'
    extra_context = {'title': 'Расписание'}

    user: CustomUserModel | None = None

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        session_user = self.request.user
        if session_user is None:
            return redirect('user:login')

        self.user = CustomUserModel.objects.filter(email=session_user).first()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any] | str:
        context = super().get_context_data(**kwargs)

        context['user_profile'] = self.user

        return context
