import pytest
from celery.result import EagerResult
from explorator.tasks.models import Task

from explorator.collectors.tests.factories import CollectorTypeFactory, CollectorFactory, Collector, CollectorType
from explorator.collectors.tasks import start_collecting

pytestmark = pytest.mark.django_db


@pytest.fixture(scope="function")
def collection_fixture_data():
    collector_type = CollectorTypeFactory()
    for item in range(4):
        CollectorFactory(collector_type=collector_type)


def test_start_collector(settings, collection_fixture_data):
    """Basic test for collector start"""
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = start_collecting.delay()
    assert isinstance(task_result, EagerResult)
    collector = Collector.objects.all()
    assert len(collector) == 4
    assert Task.objects.count() == 4
