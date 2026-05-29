import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'notifications'

        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard) (
            self.room_group_name,
            self.channel_name,
        )

    def send_notification(self, event):
        self.send(text_data=json.dumps({
            'type': 'notification',
            'title': event['title'],
            'author': event['author'],
        }))