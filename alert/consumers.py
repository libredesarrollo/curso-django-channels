import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.utils import timezone, dateformat

from .models import Alert

class AlertConsumer(WebsocketConsumer):

    def connect(self):
        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        self.user = self.scope['user']

        print("en el consumer")
        

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)
        (self.room_group_name, 
        self.channel_name)

        print("Desconectado")

    def receive(self, text_data):
        print("Recibido!")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        alert = Alert()
        alert.content = message
        alert.user = self.user

        alert.save()
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type' : 'chat_message',
                'message' : message,
                'username' : self.user.username,
                'datetime' : dateformat.format(alert.create_at, 'Y-m-d H:i:s')
            }
        )

        #print(message)
        #self.send(text_data=json.dumps({'message': message}))

    def chat_message(self, event):
        message = event['message']
        datetime = event['datetime']
        username = event['username']
        print(message)
        self.send(text_data=json.dumps({'message': message, 'username': username, 'datetime' : datetime}))