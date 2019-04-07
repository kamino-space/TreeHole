from django.db import models


class EventMsg(models.Model):
    mid = models.IntegerField()
    account = models.TextField()
    type = models.TextField()
    message = models.TextField(null=True)
    message_raw = models.TextField(null=True)
    resource = models.TextField(null=True)
    resource_remote = models.TextField(null=True)
    time = models.IntegerField()
