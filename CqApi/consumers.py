from channels.generic.websocket import WebsocketConsumer
from CqEvent.models import EventMsg
import Core
import json
import time


class ApiConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        while True:
            if Core.SQ.empty():
                continue
            message = Core.SQ.get_nowait()
            print("SEND %s" % message)
            self.send(text_data=Core.MsgBuilder.send_private_msg(1019728153, message))
