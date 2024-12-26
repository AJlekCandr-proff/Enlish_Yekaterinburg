from django.urls import path

from .views import account, login, registration


app_name = 'user'


urlpatterns = [
    path('account', account, name='account'),
    path('login', login, name='login'),
    path('registration', registration, name='registration')
]
