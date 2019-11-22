from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Trips_daily
from .forms import Trips_dailyForm, Cities_dir


def main_view(request):
    return render(request, 'trip/index.html', {})

def profile_view(request):
    greetting = 'Hey!'
    user = request.user
    full_name = user.get_full_name()
    query = User.objects.get(pk = user.pk)
    context = {
        'user':query,
        'greet':greetting,
        'full_name': user.get_full_name()
    }
    return render(request, 'account/profile.html', context)

    #Forms for creating for trips
class TripCreateView(CreateView):
    model = Trips_daily
    form_class = Trips_dailyForm
 #   fields = ('from_country', 'from_city', 'to_country', 'to_city')
    template_name = 'trip/trip_create.html'
    success_url   = reverse_lazy('home')

#View for Ajax call
def load_cities(request):
    #point FROM
    from_country_id = request.GET.get('from_country')
    from_cities     = Cities_dir.objects.filter(country_id=from_country_id).order_by('city_name')

    #point TO
    to_country_id  = request.GET.get('to_country')
    to_cities      = Cities_dir.objects.filter(country_id=to_country_id).order_by('city_name')  

    context = {
        'from_cities': from_cities,
        'to_cities'  : to_cities 
    }

    return render(request, 'trip/cities_dropdown_list_options.html', context)