from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

from .models import (Comment,
                     Trips_daily,
                     Profile,
                     User,)

from .forms import (CommentForm,
                    Trips_dailyForm,
                    Cities_dir,)

# third party importts
from rest_framework import mixins
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TripsDetailSerializer

class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Trips_daily.objects.all()
        serialize = TripsDetailSerializer(qs, many=True)
        return Response(serialize.data)

    def post(self, request, *args, **kwags):
        serializer = TripsDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner = self.request.user) # you should put user authomatically 
            return Response(serializer.data)
        return Response(serializer.errors)


class TripsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class   = TripsDetailSerializer
    queryset           = Trips_daily.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    
    

def main_view(request):
    return render(request, 'trip/index.html', {})


@login_required(login_url='account_login')
def trip_creat_view(request):
    form = Trips_dailyForm(request.POST or None)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
    if form.errors:
        errors = form.errors
    template_name = 'trip/trip_create.html'
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, template_name, context)


def list_of_trip(request):
    trips_query = Trips_daily.objects.all().order_by('-date_posted')
    template_name = 'trip/trips_list.html'
    context = {
        'trips': trips_query,
    }
    return render(request, template_name, context)


def detail_of_trip(request, id):
    trip_query = get_object_or_404(Trips_daily, id=id)
    user_query = Profile.objects.get(user = trip_query.owner)#.values('first_name')
    template_name = 'trip/trip_detail.html'
    context = {
        'trip': trip_query,
        'owner':user_query
    }
    return render(request, template_name, context)


def edit_of_trip(request, id):
    trip_query = get_object_or_404(Trips_daily, id=id)
    form = Trips_dailyForm(request.POST or None, instance=trip_query)
    if form.is_valid():
        instance = form.save(commit=False)
        if request.user == instance.owner:
            form.save()
            messages.info(request, 'Данные были обновлены')
            return redirect('../')
        else:
            return HttpResponse('This is not your post pice of shit!!!')
    template_name = 'trip/trip_create.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


def profile_view(request):
    user            = request.user
    user_info_query = User.objects.get(pk=user.pk)
    template_name   = 'account/profile.html'
    context = {
        'user'     : user_info_query,
        'full_name': user.get_full_name(),
    }
    return render(request, template_name, context)

def profile_guest_view(request, id):
    queryset_profile = get_object_or_404(Profile, id=id)
    queryset_comments = Comment.objects.filter(profile_owner = queryset_profile)
    user = request.user
    template_name = 'trip/profile_for_guests.html'
    comment_form = CommentForm(data=request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.commentator = request.user
            instance.profile_owner = queryset_profile
            instance.save()
            comment_form()
    context = {
        'owner'   : queryset_profile,
        'comments': queryset_comments,
        'form'    : comment_form,
        'user_in'     : user,
    }
    return render(request, template_name, context)



# View for Ajax call
def load_cities(request):
    # point FROM
    from_country_id = request.GET.get('from_country')
    from_cities = Cities_dir.objects.filter(country_id=from_country_id).order_by('city_name')

    # point TO
    to_country_id = request.GET.get('to_country')
    to_cities = Cities_dir.objects.filter(country_id=to_country_id).order_by('city_name')

    context = {
        'from_cities': from_cities,
        'to_cities': to_cities
    }

    return render(request, 'trip/cities_dropdown_list_options.html', context)

    # Forms for creating for trips


""" class TripCreateView(CreateView):
    model = Trips_daily
    form_class = Trips_dailyForm
 #   fields = ('from_country', 'from_city', 'to_country', 'to_city')
    template_name = 'trip/trip_create.html'
    success_url   = reverse_lazy('home') """
