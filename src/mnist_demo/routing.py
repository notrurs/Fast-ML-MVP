from django.urls import re_path

from .consumers import AppConsumer


websocket_urlpatterns = [
    re_path(r'ws_draw/', AppConsumer.as_asgi())
]
