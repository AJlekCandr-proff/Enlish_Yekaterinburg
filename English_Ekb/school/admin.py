from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models.teachers import Teachers


@admin.register(Teachers)
class TeachersAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name', 'patronymic']
