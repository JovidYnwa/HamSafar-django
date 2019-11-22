from django.urls import path
from .views import (main_view,
                    profile_view,
                    TripCreateView,
                    load_cities)

urlpatterns = [
    path('main/', main_view, name='home'),
    path('accounts/profile/', profile_view,  name='account_profile'),

    path('add/', TripCreateView.as_view()),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]

