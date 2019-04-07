from channels.generic.websocket import WebsocketConsumer
from CqEvent.models import EventMsg
import Core
import json


class ApiConsumer(WebsocketConsumer):

    def receive(self, text_data=None, bytes_data=None):
        print('API: %s' % text_data)
