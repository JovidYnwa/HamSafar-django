from django.urls import path, include
from .views import (main_view,
                    profile_view,
                    profile_guest_view,
                    #TripCreateView,
                    trip_creat_view,
                    load_cities,
                    list_of_trip,
                    detail_of_trip,
                    edit_of_trip,
                    #APIVIEWS   
                    TestView,
                    TripsDetailView,
            )

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

#app_name = 'trip'
urlpatterns = [
    path('main/', main_view, name='home'),
    path('accounts/profile/', profile_view,  name='account_profile'),
    path('trip/profile/<int:id>/', profile_guest_view, name='profile_guest_view'),
    path('trips/', list_of_trip, name='list_of_trips'),
    path('trip/<int:id>/', detail_of_trip, name='detail_of_trip'),
    path('trip/<int:id>/edit/', edit_of_trip, name='edit_of_trip'),
    #path('add/', TripCreateView.as_view(), name='trip-create'),
    path('trip-create/', trip_creat_view, name='trip-create'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),

    #If you're intending to use the browsable API you'll probably also want to add REST framework's
    #login and logout views
    path('api/docs/', include_docs_urls(title='HamSafar API')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('api/trip_create/', TestView.as_view(), name = 'trip-list'),
    path('api/trip-detail/<int:pk>/', TripsDetailView.as_view(), name = 'trip-detail'),
]

