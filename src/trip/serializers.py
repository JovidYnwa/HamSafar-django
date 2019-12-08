from rest_framework import serializers

from .models import Trips_daily, User

class TripsDetailSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    settle_date = serializers.DateTimeField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = Trips_daily
        fields = '__all__'


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