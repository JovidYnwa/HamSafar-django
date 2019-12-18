from rest_framework import serializers

from .models import Trips_daily, User


class TripsDetailSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    settle_date = serializers.DateTimeField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = Trips_daily
        fields = '__all__'


