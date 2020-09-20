import pytest
from celery.result import EagerResult

from explorator.collectors.tests.factories import CollectorTypeFactory
from explorator.collectors.tasks import start_collecting

pytestmark = pytest.mark.django_db


def test_start_collector(settings):
    """Basic test for collector start"""
    CollectorTypeFactory.create_batch(4)
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = start_collecting.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == 4
