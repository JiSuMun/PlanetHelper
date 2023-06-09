from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('<int:user_id>/', views.start_chat, name='start_chat'),
    path('start_group_chat/', views.start_group_chat, name='start_group_chat'),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/delete/', views.delete_chat, name='delete_chat'),
    path('api/unread_notifications/', views.unread_notifications, name='unread_notifications'),
    path('api/new_chat_rooms/', views.get_new_chat_rooms, name='new_chat_rooms'),
]