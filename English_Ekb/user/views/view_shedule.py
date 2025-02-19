from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView


class ScheduleView(UpdateView):
    template_name = 'user/pages/schedule.html'
    extra_context = {'title': 'Расписание'}

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user is None:
            return redirect('user:login')

        return super().dispatch(request, *args, **kwargs)
