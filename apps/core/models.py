from django.db import models


# Create your models here.
class SensorType(models.Model):
    name = models.CharField(max_length=255)  # Distance, light and etc...

    def __str__(self):
        return '%s' % (self.name)


class Sensor(models.Model):
    """
    Description: Sensor Description
    """
    name = models.CharField(max_length=255)
    sensor_model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    min_value = models.FloatField()
    max_value = models.FloatField()
    sensor_type = models.ForeignKey(SensorType, related_name='+')

    def __str__(self):
        return '%s' % (self.name)


class Property(models.Model):
    BOUNDARIES = (
        ('eq', 'Equals'),
        ('gt', 'Grater than'),
        ('lt', 'Less than')
    )
    name = models.CharField(max_length=255)
    value = models.FloatField()
    unity = models.CharField(max_length=10)
    boundary = models.CharField(max_length=2, choices=BOUNDARIES)
    sensor = models.ForeignKey(Sensor, related_name='properties')

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return '%s: |%s %f %s ' % (self.name, self.boundary, self.value, self.boundary)


class Log(models.Model):
    date = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    value = models.FloatField()
    unity = models.CharField(max_length=10)
    sensor_id = models.IntegerField()  # Don't want a relationship
    # sensor_type

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{date:%Y/%m/%d %H:%M:%S} - longitude: {longitude}, latitude: {latitude} - {value:.2f} {unity}' \
            .format(date=self.date, longitude=self.longitude, latitude=self.latitude, value=self.value, unity=self.unity)


