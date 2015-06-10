from django.contrib import admin
from .models import Sensor
from .models import Property
from .models import Log
from .models import SensorType
# from .forms import SensorModelForm


# Register your models here.
class PropertyInline(admin.TabularInline):
    model = Property
    extra = 1


class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SensorType, SensorTypeAdmin)


# class SensorTypeInline(admin.TabularInline):
#     model = SensorType
#     # model = SensorType.sensor.through


class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'sensor_type', 'sensor_model', 'manufacturer',
            'min_value', 'max_value']
    fields = ('name', 'sensor_type', 'sensor_model', 'manufacturer',
            'min_value', 'max_value')
    inlines = (
        PropertyInline,
    )
    # form = SensorModelForm

admin.site.register(Sensor, SensorAdmin)


class PropertyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Property, PropertyAdmin)


class LogAdmin(admin.ModelAdmin):
    # fields = ('sensor_id', 'latitude', 'longitude', 'value', 'unity')
    readonly_fields = ['date', 'sensor_id', 'latitude', 'longitude', 'value', 'unity']
    list_display = ['get_date', 'get_sensor', 'latitude', 'longitude', 'value', 'unity']
    list_display_links = ('get_date',)
    list_filter = ('date',)
    # readonly_fields = ['date']
    # date_hierarchy = 'date'
    actions = None

    def has_add_permission(self, request):
        # Nobody is allowed to add
        return True

    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        return False

    # def has_change_permission(request, obj=None):
    #     return False

    def get_date(self, obj):
        return obj.date.strftime("%d/%m/%Y %H:%M:%S")
    get_date.admin_order_field = 'date'
    get_date.short_description = 'Date'

    def get_sensor(self, obj):
        return Sensor.objects.get(pk=obj.sensor_id)
    # get_sensor.admin_order_field = 'sensor'
    get_sensor.short_description = 'Sensor'

admin.site.register(Log, LogAdmin)
