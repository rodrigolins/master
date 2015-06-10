from .models import Sensor
from .models import Property
from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'sensor_model', 'manufacturer', 'min_value', 'max_value')


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('name', 'value', 'unity', 'boundary', 'sensor')
