from django.urls import path
from .views import main_view, profile_view

urlpatterns = [
    path('main/', main_view, name='home'),
    path('accounts/profile/', profile_view,  name='account_profile')
]