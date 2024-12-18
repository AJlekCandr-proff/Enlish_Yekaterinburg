from django.urls import path

from .views import index, teachers, account

app_name = 'school'


urlpatterns = [
    path('', index, name='index'),
    path('teachers', teachers, name='teachers'),
    path('account', account, name='account')
]
