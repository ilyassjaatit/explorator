from django.db import models
from jsonfield import JSONField

from explorator.collectors.models import Collector


class Task(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE)
    raw_data = JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Queue(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    process = models.CharField(max_length=255, null=True)
    finished = models.DateTimeField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
