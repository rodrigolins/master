from rest_framework import viewsets
from .serializers import SensorSerializer
from .serializers import PropertySerializer
from .models import Sensor
from .models import Property


# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(sensor_type__name=q)
        return queryset


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
