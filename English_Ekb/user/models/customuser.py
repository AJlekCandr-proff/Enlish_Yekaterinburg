from django.contrib.auth.models import AbstractBaseUser
from django.db.models import CharField, EmailField, BooleanField, ForeignKey, SET_NULL

from ..managers.manager_user import UserManager
from .students import Students
from .teachers import Teachers


class CustomUser(AbstractBaseUser):
    first_name = CharField(verbose_name='Имя')
    last_name = CharField(verbose_name='Фамилия')
    patronymic = CharField(verbose_name='Отчество', blank=True)

    password = CharField(max_length=15, verbose_name='Пароль от аккаунта')
    mail = EmailField(verbose_name='Электронная почта', unique=True)
    phone = CharField(verbose_name='Номер телефона', blank=True)

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    role = ForeignKey(Students or Teachers, on_delete=SET_NULL, blank=True, null=True)

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic', 'phone']

    objects = UserManager()

    class Meta:
        db_table_comment = 'Table with users.'
        db_table = 'users'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.mail
