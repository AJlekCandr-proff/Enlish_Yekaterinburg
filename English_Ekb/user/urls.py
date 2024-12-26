from django.urls import path

from .views import account, registration, LoginCustomView


app_name = 'user'


urlpatterns = [
    path('account/', account, name='account'),
    path('login/', LoginCustomView.as_view(), name='login'),
    path('registration/', registration, name='registration')
]
