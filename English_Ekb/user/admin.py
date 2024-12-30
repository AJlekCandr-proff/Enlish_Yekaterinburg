from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models import *


@admin.register(Students)
class StudentsAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = []


@admin.register(Teachers)
class StudentsAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = []


@admin.register(Administrator)
class StudentsAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = []
