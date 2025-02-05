from django.forms import Form, CharField


class ConfirmationCodeForm(Form):
    code = CharField(max_length=6, label='Код подтверждения')
