from django.urls import path

from .views import index

app_name = 'school'


urlpatterns = [path('', index, name='index')]
