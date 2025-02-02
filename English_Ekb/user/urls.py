from django.urls import path

from .views import *


app_name = 'user'


urlpatterns = [
    path('account/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/confirm', name='login-confirm'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('registration/confirm', name='registration-confirm')
]
