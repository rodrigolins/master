from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
#router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
