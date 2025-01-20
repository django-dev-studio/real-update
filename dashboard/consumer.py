from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DashboardAnalytics(AsyncWebsocketConsumer):
    group_name = 'analytics'

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print('Received sensor data', text_data)
        _data = json.loads(text_data)
        _date_value = _data['value']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'processed_data',
                'data': _date_value
            }
        )

    async def processed_data(self, events):
        _value = events['data']
        await self.send(text_data=json.dumps({'processed': _value}))