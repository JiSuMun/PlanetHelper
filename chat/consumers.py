import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Message, Notification
from django.contrib.auth import get_user_model

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # 한글이라 깨지는 문제 발생 해결
        self.room_group_name = 'aa'
        # name = [ord(char) for char in self.room_name]
        # b = ''
        # for a in name:
        #     b += str(a)
        
        # self.room_group_name = f'chat{b}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_image_url, formatted_timestamp = await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].first_name,
                'sender_image_url': sender_image_url,
                'formatted_timestamp': formatted_timestamp,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        sender_image_url = event['sender_image_url']
        formatted_timestamp = event['formatted_timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'formatted_timestamp': formatted_timestamp,
            'sender_image_url': sender_image_url,
        }))


    @database_sync_to_async
    def save_message(self, message):
        chat_room = ChatRoom.objects.get(name=self.room_name)
        sender = self.scope['user']
        new_message = Message(chat_room=chat_room, sender=sender, content=message)
        new_message.save()
        formatted_timestamp = new_message.formatted_timestamp()
        sender_image_url = str(sender.image.url) if sender.image else '/static/img/accounts/no-image-icon-21.png'
        participants = chat_room.participants.exclude(id=sender.id)
        for participant in participants:
            notification = Notification(user=participant, chat_room=chat_room, message=new_message)
            notification.save()
        return sender_image_url, formatted_timestamp
    
    @database_sync_to_async
    def get_or_create_room(self, user_ids):
        users = get_user_model().objects.filter(id__in=user_ids)
        chat_room = ChatRoom.get_or_create_chat_room(users)
        return chat_room
