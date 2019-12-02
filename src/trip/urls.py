from django.urls import path
from .views import (main_view,
                    profile_view,
#                    TripCreateView,
                    trip_creat_view,
                    load_cities,
                    list_of_trip,
                    detail_of_trip,
                    edit_of_trip,
                    )


urlpatterns = [
    path('main/', main_view, name='home'),
    path('accounts/profile/', profile_view,  name='account_profile'),
    path('trips/', list_of_trip, name='list_of_trips'),
    path('trip/<int:id>/', detail_of_trip, name='detail_of_trip'),
    path('trip/<int:id>/edit/', edit_of_trip, name='edit_of_trip'),
#   path('add/', TripCreateView.as_view(), name='trip_add'),
    path('add/', trip_creat_view, name='trip_add'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]

