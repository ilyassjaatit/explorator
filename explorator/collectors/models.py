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
    """
        Run the collector based on a recipe.

        Attributes
        ----------
        name: string not null
        collector_type: `collector_type`
        recipe: dict not null
            "examples": [
                {
                    "jobs": {
                        "find_urls": {
                            "save": true,
                            "new_jobs": true,
                            "domains_allowed": [
                                "www.python.org",
                                "es.wikipedia.org"
                            ]
                        },
                        "headers": {
                            "save": true
                        }
                    }
                }
            ],
            "required": [
                "jobs"
            ]
        frequency: int
        created_at: DateTime
            creation date

        updated_at: DateTime
            update date
    """
    name = models.CharField(max_length=255)
    collector_type = models.ForeignKey(CollectorType, on_delete=models.CASCADE)
    recipe = JSONField(null=True)
    frequency = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
