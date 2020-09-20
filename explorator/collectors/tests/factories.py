from factory import Faker, post_generation
from factory.django import DjangoModelFactory
from explorator.collectors.models import CollectorType

class CollectorTypeFactory(DjangoModelFactory):
    name = Faker('name')
    type = CollectorType.WEB_SCRAPING
    class Meta:
        model = CollectorType
