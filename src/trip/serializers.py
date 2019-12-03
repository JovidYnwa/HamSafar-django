from rest_framework import serializers

from .models import Trips_daily, User

class Trips_dailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips_daily
        fields = (
            'owner',
            'from_country',
            'from_city',
            'to_country',
            'to_city',
            'description',
            'date_posted',
            'price',
            'settle_date'
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user