from channels.generic.websocket import WebsocketConsumer
from CqEvent.models import EventMsg
import Core
import json
import time


class ApiConsumer(WebsocketConsumer):

    def receive(self, text_data=None, bytes_data=None):
        pass
        # print("API RETURN %s" % text_data)
