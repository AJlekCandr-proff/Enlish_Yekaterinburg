from django.urls import path

from .views import *


app_name = 'school'


urlpatterns = [
    path('', index, name='index'),
    path('teachers', teachers, name='teachers'),
    path('account', account, name='account'),
    path('login', login, name='login'),
    path('registration', registration, name='registration')
]
