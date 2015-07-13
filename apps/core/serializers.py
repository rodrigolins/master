from .models import Sensor
from .models import SensorType
from .models import Property
from .models import PropertyType
from rest_framework import serializers


class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('name',)


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    property_type = PropertyTypeSerializer()

    class Meta:
        model = Property
        fields = ('property_type', 'value', 'unit', 'boundary',)


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ('name',)


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    sensor_type = SensorTypeSerializer()
    properties = PropertySerializer(many=True)

    class Meta:
        model = Sensor
        fields = ('sensor_type', 'model', 'manufacturer', 'properties',)
