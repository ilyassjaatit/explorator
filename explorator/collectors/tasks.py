from config import celery_app

from explorator.collectors.models import CollectorType

@celery_app.task()
def start_collecting():
    """start  collecting"""
    return CollectorType.objects.count()
