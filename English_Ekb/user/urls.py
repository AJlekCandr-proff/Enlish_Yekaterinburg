from django.urls import path

from .views import registration, LoginCustomView, UserProfileView


app_name = 'user'


urlpatterns = [
    path('account/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginCustomView.as_view(), name='login'),
    path('registration/', registration, name='registration')
]
