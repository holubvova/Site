from channels.generic.websocket import AsyncWebsocketConsumer
import json


class AdminNotificationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("admin_notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("admin_notifications", self.channel_name)

    async def admin_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            'queue': message['queue'],
            'name': message['name'],
            'data': message['data'],
            'result': message['result'],
            'timestamp': message['timestamp'],
            'recipient': message['recipient'],
        }))
