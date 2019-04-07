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
        try:
            message = json.loads(text_data)
        except Exception as e:
            print(e)
            self.close()
            return None
        if message['self_id'] != CORE_SETTING['robot']:
            self.close()
            return None
        try:
            save = EventMsg(
                mid=message['message_id'],
                account=message['user_id'],
                type=message['message_type'],
                message=message['message'],
                resource=None,
                time=message['time'],
            )
            save.save()
        except Exception as e:
            print(e)
