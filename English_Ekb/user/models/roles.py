from django.db.models import Model, CharField, ForeignKey, CASCADE
from .users import CustomUserModel


class Student(Model):
    user = ForeignKey(CustomUserModel, on_delete=CASCADE)
    teacher = CharField(max_length=25, verbose_name='ФИО предподавателя')

    class Meta:
        db_table_comment = 'Table with student role.'
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self) -> str:
        return self.teacher


class Teacher(Model):
    user = ForeignKey(CustomUserModel, on_delete=CASCADE)
    experience = CharField(verbose_name='Опыт предподавателя')

    class Meta:
        db_table_comment = 'Table with teachers.'
        db_table = 'teachers'
        verbose_name = 'предподаватель'
        verbose_name_plural = 'предподаватели'

    def __str__(self) -> str:
        return self.experience
