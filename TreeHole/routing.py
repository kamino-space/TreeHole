from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from CqEvent.consumers import EventConsumer
from CqApi.consumers import ApiConsumer

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("event", EventConsumer),
            url("api", ApiConsumer),
        ])
    )
})
