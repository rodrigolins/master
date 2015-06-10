from django import forms
from .models import Sensor


# class SensorModelForm(forms.ModelForm):
#     fields = ('name', 'sensor_type', 'sensor_model', 'manufacturer',
#             'min_value', 'max_value', 'properties')
#     class Meta:
#         model = Sensor
#         widgets = {
#             'properties': forms.SelectMultiple(attrs={'size': 12})
#         }
