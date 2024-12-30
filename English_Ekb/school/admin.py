from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models.lessons import Lessons


@admin.register(Lessons)
class LessonsAdmin(ModelAdmin):
    list_display = ['title']
