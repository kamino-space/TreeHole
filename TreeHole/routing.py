from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from CqApi.consumers import ApiConsumer
from CqEvent.consumers import EventConsumer

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("api", ApiConsumer),
            url("event", EventConsumer),
        ])
    )
})
