from django.db import models

# Create your models here.
class Station(models.Model):
    stations = models.ForeignKey('StationIndex')
    file_name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    def __unicode__(self):
       return u"%s - (%s - %s)" % (self.file_name, self.longitude, self.latitude)

class Model(models.Model):
    TYPE = (
        ('FORECAST', 'Forecast'),
        ('HINDCAST', 'Hindcast'),
    )
    web_url = models.URLField()
    name = models.CharField(max_length=30)
    order = models.IntegerField()
    display_title = models.CharField(max_length=100)
    model_type = models.CharField(max_length=15, choices=TYPE,
                                  default='HINDCAST')
    time_series = models.BooleanField(blank=True)
    center_longitude = models.IntegerField()
    center_latitude = models.IntegerField()
    zoom_level = models.IntegerField()
    station = models.ForeignKey('StationIndex', null=True, blank=True)
    published = models.BooleanField()
    def __unicode__(self):
        return u"%s - %s" % (self.name, self.display_title)

class StationIndex(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    web_folder_url = models.URLField()
    icon = models.ImageField(upload_to="icon/")

    def __unicode__(self):
        return self.name

class Variable(models.Model):
    model = models.ForeignKey('Model')
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=60)
    NCDF_variable = models.CharField(max_length=60)
    order = models.IntegerField(blank=True)
    def __unicode__(self):
        return u"%s - %s - %s" % (self.model.name, self.name, self.NCDF_variable)

class Type(models.Model):
    variable = models.ForeignKey('Variable')
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=60)
    style = models.CharField(max_length=60, help_text="WMS types, current have vectors, contours, fileedcontours, facets, pcolor")
    order = models.IntegerField(blank=True)
    def __unicode__(self):
        return u"%s - %s - %s" % (self.variable.model.name, self.variable.name, self.name)

class Value(models.Model):
    type = models.ForeignKey('Type')
    name = models.CharField(max_length=60, help_text="These name can be arrow_size, arrow_width, color as defult")
    display_name = models.CharField(max_length=60)
    value = models.CharField(max_length=60, help_text="can be 40, 50, jet")
    order = models.IntegerField(blank=True)
    def __unicode__(self):
       return u"%s - %s - %s - %s" % (self.type.variable.model.name, self.type.variable.name, self.type.name, self.name)
