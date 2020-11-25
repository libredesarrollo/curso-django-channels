from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/alert/room/<room_id>', consumers.AlertConsumer.as_asgi()),
]