from django.db.models import Model, CharField, ForeignKey, CASCADE, ManyToManyField
from .users import CustomUserModel


class Lessons(Model):
    DAYS = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье')
    ]

    topic = CharField(verbose_name='Тема урока', blank=True)
    users = ManyToManyField(CustomUserModel, verbose_name='Ученики', related_name='students_profile')
    teacher = ForeignKey(CustomUserModel, on_delete=CASCADE, verbose_name='Предподаватель', related_name='teacher_profile')
    link = CharField(verbose_name='Ссылка на урок', blank=True)

    day_of_week = CharField(
        choices=DAYS,
        verbose_name='День недели'
    )

    class Meta:
        db_table_comment = 'Table with lessons.'
        db_table = 'lessons'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self) -> str:
        return self.topic
