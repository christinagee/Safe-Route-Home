from __future__ import unicode_literals

from django.db import models


# Create your models here.


class CrimeDataPoint(models.Model):
    incident_number = models.CharField(
        'INCIDENT NUMBER',
        max_length=120,
        blank=True,
        null=True
    )
    offense_codd = models.IntegerField(
        'OFFENSE CODE',
        blank=True,
        null=True
    )
    offense_code_group = models.CharField(
        'OFFENSE CODE GROUP',
        max_length=120,
        blank=True,
        null=True
    )
    offense_description = models.CharField(
        'OFFENSE DESCRIPTION',
        max_length=120,
        blank=True,
        null=True
    )
    district = models.CharField(
        'DISTRICT',
        max_length=120,
        blank=True,
        null=True
    )
    reporting_area = models.CharField(
        'REPORTING AREA',
        max_length=120,
        blank=True,
        null=True
    )
    occurred_on_date = models.DateTimeField(
        'OCCURRED ON DATE',
        blank=True,
        null=True
    )
    hour = models.IntegerField(
        'HOUR',
        blank=True,
        null=True
    )
    year = models.IntegerField(
        'YEAR',
        blank=True,
        null=True
    )
    month = models.IntegerField(
        'MONTH',
        blank=True,
        null=True
    )
    day_of_week = models.CharField(
        'DAY OF WEEK',
        max_length=120,
        blank=True,
        null=True
    )
    ucr_part = models.CharField(
        'UCR PART',
        max_length=120,
        blank=True,
        null=True
    )
    street = models.CharField(
        'STREET',
        max_length=120,
        blank=True,
        null=True
    )
    latitude = models.FloatField(
        'LATITUDE',
        blank=True,
        null=True,

    )
    longitude = models.FloatField(
        'LONGITUDE',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)
