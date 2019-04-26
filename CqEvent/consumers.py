from channels.generic.websocket import WebsocketConsumer
from CqEvent.models import EventMsg
from TreeHole.settings import CORE_SETTING
import Core
import json


class EventConsumer(WebsocketConsumer):
    example = {"font": 9094328,
               "message": "测试",
               "message_id": 48,
               "message_type": "private",
               "post_type": "message",
               "raw_message": "测试",
               "self_id": 1638393029,
               "sender": {
                   "age": 20,
                   "nickname": "onimak",
                   "sex": "male",
                   "user_id": 1019728153
               },
               "sub_type": "friend",
               "time": 1554549781,
               "user_id": 1019728153
               }

    def receive(self, text_data=None, bytes_data=None):
        print('EVENT: %s' % text_data)
