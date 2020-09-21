from django.db import models
from jsonfield import JSONField

class CollectorType(models.Model):
    """Definition of the collector type"""
    API = "API"
    WEB_SCRAPING = "WS"
    TYPE_CHOICES = [
        (API, 'Api'),
        (WEB_SCRAPING, 'Web scraping')
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Collector(models.Model):
    """Run the collector based on a recipe."""
    name = models.CharField(max_length=255)
    collector_type = models.ForeignKey(CollectorType, on_delete=models.CASCADE)
    recipe = JSONField(null=True)
    frequency = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
