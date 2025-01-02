from django.db.models import CharField, ImageField, PositiveSmallIntegerField, Model, EmailField


class Students(Model):
    first_name = CharField(verbose_name='Имя')
    last_name = CharField(verbose_name='Фамилия')
    patronymic = CharField(verbose_name='Отчество', blank=True)

    password = CharField(max_length=15, verbose_name='Пароль от аккаунта')
    mail = EmailField(verbose_name='Электронная почта', unique=True)
    phone = CharField(verbose_name='Номер телефона', blank=True)

    age = PositiveSmallIntegerField(verbose_name='Возраст', blank=True)
    full_name_teacher = CharField(verbose_name='ФИО преподавателя', blank=True)
    avatar = ImageField(verbose_name='Фото профиля', blank=True)

    class Meta:
        db_table_comment = 'Table with student accounts.'
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
