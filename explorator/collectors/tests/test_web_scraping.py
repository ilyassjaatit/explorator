import pytest
from explorator.collectors.web_scraping import *
from explorator.collectors.tests.factories import CollectionFactory

pytestmark = pytest.mark.django_db


def test_headers():
    assert headers() == "When I start working?"


def test_find_urls():
    assert find_urls() == "When I start working?"


@pytest.mark.django_db
class TestWebScraping:

    def test_create_queue_job(self):
        collector = CollectionFactory()
        web_scraping = WebScrapingCollector(collector)
        queue_job = web_scraping.create_queue_job()
        assert len(queue_job) == 2
        assert queue_job == {'find_urls': True, 'headers': True}
