from factory import Faker, post_generation, SubFactory
from factory.django import DjangoModelFactory
from explorator.collectors.models import CollectorType, Collector

RECIPE = {
    "jobs": {
        "find_urls": {
            "save": True,
            "new_jobs": True,
            "domains_allowed": [
                "www.python.org"
            ]
        },
        "headers": {
            "save": True
        }
    }
}


class CollectorTypeFactory(DjangoModelFactory):
    name = Faker('name')
    type = CollectorType.WEB_SCRAPING

    class Meta:
        model = CollectorType


class CollectionFactory(DjangoModelFactory):
    name = Faker('name')
    recipe = RECIPE
    frequency = 320
    collector_type = SubFactory(CollectorTypeFactory)
    class Meta:
        model = Collector
