from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models import *


@admin.register(Students)
class StudentsAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = []


@admin.register(Lessons)
class LessonsAdmin(ModelAdmin):
    list_display = ['title']
