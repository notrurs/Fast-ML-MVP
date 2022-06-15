import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import mnist_demo.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fast-ml-mvp.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            mnist_demo.routing.websocket_urlpatterns
        )
    )
})
