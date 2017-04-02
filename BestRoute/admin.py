from django.contrib import admin

from BestRoute.models import CrimeDataPoint
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.


class CrimeDataPointResource(resources.ModelResource):

    class Meta:
        model = CrimeDataPoint


class CrimeDataPointAdmin(ImportExportActionModelAdmin):
    resource_class = CrimeDataPointResource

admin.site.register(CrimeDataPoint, CrimeDataPointAdmin)
