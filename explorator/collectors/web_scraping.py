"""Data collector with web scraping"""
from explorator.collectors.models import Collector

def headers ():
    return "When I start working?"

def find_urls():
     return "When I start working?"

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



