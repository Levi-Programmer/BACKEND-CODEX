from rest_framework import serializers
from .models import User, City, Trajectory, horizon

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class TrajectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajectory
        fields = '__all__'
