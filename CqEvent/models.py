from django.db import models


class EventMsg(models.Model):
    mid = models.IntegerField()
    account = models.TextField()
    type = models.TextField()
    message_text = models.TextField(null=True)
    message_raw = models.TextField(null=True)
    resource_local = models.TextField(null=True)
    resource_remote = models.TextField(null=True)
    time = models.IntegerField()
