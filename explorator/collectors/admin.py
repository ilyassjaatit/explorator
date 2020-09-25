from django.contrib import admin

from explorator.collectors.models import CollectorType, Collector

admin.site.register(CollectorType)
admin.site.register(Collector)
