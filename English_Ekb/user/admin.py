from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models import CustomUserModel


@admin.register(CustomUserModel)
class UsersAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'email']
