from django.urls import path

from .views import LoginUserView, UserProfileView


app_name = 'user'


urlpatterns = [
    path('account/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    # path('registration/', RegistrationCustomView.as_view(), name='registration')
]
