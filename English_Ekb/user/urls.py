from django.urls import path

from .views import *


app_name = 'user'


urlpatterns = [
    path('account/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/<str:email>', ConfirmMailView.as_view(), name='login-confirm'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('registration/<str:email>', ConfirmMailView.as_view(), name='registration-confirm'),
    path('schedule/', ScheduleView.as_view(), name='schedule')
]
