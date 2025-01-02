from django.db.models import CharField, ImageField, PositiveSmallIntegerField, Model, EmailField


class Teachers(Model):
    first_name = CharField(verbose_name='Имя')
    last_name = CharField(verbose_name='Фамилия')
    patronymic = CharField(verbose_name='Отчество', blank=True)

    password = CharField(max_length=15, verbose_name='Пароль от аккаунта')
    mail = EmailField(verbose_name='Электронная почта', unique=True)
    phone = CharField(verbose_name='Номер телефона', blank=True)

    age = PositiveSmallIntegerField(verbose_name='Возраст', blank=True)
    full_name_teacher = CharField(verbose_name='ФИО преподавателя', blank=True)
    avatar = ImageField(verbose_name='Фото профиля', blank=True)

    about_teacher = CharField(max_length=350, verbose_name='О себе')
    experience = CharField(verbose_name='Опыт преподавания')

    class Meta:
        db_table_comment = 'Table with teacher accounts.'
        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
