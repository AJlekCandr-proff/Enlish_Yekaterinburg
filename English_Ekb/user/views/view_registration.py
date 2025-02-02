from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.conf import settings

from ..forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm

    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}

    def form_valid(self, form):
        user = form.save()

        subject = "Welcome to Our Site!"
        message = f"Thank you for registering, {user.username}!"

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user:registration-confirm')