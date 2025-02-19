from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField, BooleanField

from ..managers.user_manager import CustomUserManager


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    ROLE = [
        ('Teacher', 'Предподаватель'),
        ('Student', 'Студент')
    ]

    first_name = CharField(verbose_name='Имя')
    last_name = CharField(verbose_name='Фамилия')
    patronymic = CharField(verbose_name='Отчество', blank=True)

    password = CharField(max_length=120, verbose_name='Пароль от аккаунта')
    email = EmailField(verbose_name='Электронная почта', unique=True)
    phone = CharField(verbose_name='Номер телефона', blank=True)

    code_from_mail = CharField(verbose_name='Код, отправленный по почту', blank=True)

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    role = CharField(choices=ROLE, verbose_name='Роль пользователя', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table_comment = 'Table with users.'
        db_table = 'users'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
