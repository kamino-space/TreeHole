from channels.generic.websocket import WebsocketConsumer
from CqEvent.models import EventMsg
import Core
import json
import time


class ApiConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        while Core.SQ.empty() == False:
            message = Core.SQ.get_nowait()
            print("API SEND %s" % message)
            self.send(text_data=Core.MsgBuilder.send_private_msg(1019728153, message))

    def receive(self, text_data=None, bytes_data=None):
        print("API RETURN %s" % text_data)
