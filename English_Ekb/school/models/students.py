from django.db.models import Model, CharField, ImageField, EmailField, PositiveSmallIntegerField


class Students(Model):
    first_name = CharField(verbose_name='Имя')
    last_name = CharField(verbose_name='Фамилия')
    patronymic = CharField(verbose_name='Отчество')
    age = PositiveSmallIntegerField(verbose_name='Возраст')
    full_name_teacher = CharField(verbose_name='ФИО предподавателя')
    avatar = ImageField(verbose_name='Фото профиля')
    password = CharField(max_length=15, verbose_name='Пароль от аккаунта')
    mail = EmailField(verbose_name='Электронная почта')
    phone = EmailField(verbose_name='Номер телефона')

    class Meta:
        db_table_comment = 'Table with student accounts.'
        db_table = 'students'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

