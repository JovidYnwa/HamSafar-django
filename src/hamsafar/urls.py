from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trip.urls')),
    path('accounts/', include('allauth.urls')),
]

from django.conf import settings

if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
