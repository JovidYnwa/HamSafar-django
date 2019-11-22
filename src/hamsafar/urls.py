from django.contrib import admin
from django.urls import path, include

#import static from settigns.py
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trip.urls')),
    path('accounts/', include('allauth.urls')),

]
