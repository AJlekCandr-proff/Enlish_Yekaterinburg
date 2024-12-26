from django.urls import path

from .views import index, teachers


app_name = 'school'


urlpatterns = [
    path('', index, name='index'),
    path('teachers', teachers, name='teachers')
]
