from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path('', include('school.urls', namespace='home')),
    path('teachers', include('school.urls', namespace='teachers')),
    path('account', include('user.urls', namespace='account')),
    path('login', include('user.urls', namespace='login')),
    path('registration', include('user.urls', namespace='registration'))
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
