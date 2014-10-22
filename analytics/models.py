from django.db import models
from django.db.models import URLField
from localflavor.us.models import USStateField


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        unique_together = ['city', 'country', 'region']

    def __unicode__(self):
        return u"{}, {} {}".format(self.city, self.region, self.country)


class View(models.Model):
    date = models.DateField(auto_now_add=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    page = models.ForeignKey(Page)
    location = models.ForeignKey(Location, related_name='view', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return u"{} {}".format(self.location, self.ip_address)
    #django local flavor to show us states

