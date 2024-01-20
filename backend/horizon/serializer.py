from rest_framework import serializers
from .models import Horizon

class HorizonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horizon
        fields = '__all__'