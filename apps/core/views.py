from rest_framework import viewsets
from .serializers import SensorSerializer
from .serializers import PropertySerializer
from .models import Sensor
from .models import Property


# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
