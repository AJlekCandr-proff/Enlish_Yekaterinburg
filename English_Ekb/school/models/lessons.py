from django.db.models import Model, DateField, FileField, CharField, URLField, ManyToManyField

from .students import Students


class Lessons(Model):
    title = CharField(max_length=25, verbose_name='Тема урока')
    date = DateField(verbose_name='Дата урока')
    optional_material = FileField(verbose_name='Материал к уроку')
    teacher_name = CharField(verbose_name='ФИО предподавателя')
    link_to_lesson = URLField(verbose_name='Ссылка на урок (конференцию)')
    pupils = ManyToManyField(Students, related_name='lessons', verbose_name='Ученики')

    class Meta:
        db_table_comment = 'Table with lessons.'
        db_table = 'lessons'
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self) -> str:
        return self.title
