from django.views.generic import CreateView


class RegistrationUserView(CreateView):
    template_name = 'user/pages/registration.html'
    extra_context = {'title': 'Регистрация нового пользователя'}
