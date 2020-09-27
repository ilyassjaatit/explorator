"""Data collector with web scraping"""
from explorator.collectors.models import Collector


def headers():
    return "When I start working?"


def find_urls():
    return "When I start working?"


def create_web_scraping_seeds(collector):
    for seed in collector.recipe['seeds']:
        create_web_scraping_task(collector, url=seed)
    return True


def create_web_scraping_task(collector, url):
    from explorator.collectors.tasks import Task
    new_task = Task(collector=collector, raw_data={"url": url, "process": ""})
    new_task.save()
    return new_task


class WebScrapingCollector:
    """Web Scraping"""

    def __init__(self, collector: Collector):
        self.collector = collector

    def create_queue_job(self) -> dict:
        """"""
        queued_jobs = {}
        for key, value in self.collector.recipe['jobs'].items():
            queued_jobs[key] = True
        return queued_jobs
