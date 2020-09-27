from config import celery_app

from explorator.collectors.models import CollectorType, Collector
from explorator.tasks.models import Task
from explorator.collectors.web_scraping import create_web_scraping_seeds


@celery_app.task()
def start_collecting():
    """start  collecting"""
    collectors = Collector.objects.all()
    for collector in collectors:
        tasks = Task.objects.filter(collector=collector.pk)
        if not tasks:
            if collector.collector_type.type == CollectorType.WEB_SCRAPING:
                create_web_scraping_seeds(collector)
