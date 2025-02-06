from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from ..forms import ConfirmationCodeForm
from ..models import CustomUserModel


class ConfirmMailView(FormView):
    template_name = 'user/pages/mail.html'

    form_class = ConfirmationCodeForm
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form, **kwargs):
        entered_code = form.cleaned_data.get('code')

        user = CustomUserModel.objects.get(email=kwargs.get('email'))

        if entered_code == user.code_from_mail:
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            user = get_object_or_404(CustomUserModel, email=kwargs.get('email'))

        except CustomUserModel.DoesNotExist:
            raise Http404("Пользователь не найден")

        context['title'] = f'Подтверждение почты {user.email}'

        return context
