from rest_framework import serializers
from .models import Dispense

class DispenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispense
        # fields=('productname', 'price', 'dispensing_time', 'stop_dispensing_time')
        fields= "__all__"
