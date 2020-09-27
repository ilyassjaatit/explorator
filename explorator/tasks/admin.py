from django.contrib import admin

from explorator.tasks.models import Queue, Task

admin.site.register(Queue)
admin.site.register(Task)
