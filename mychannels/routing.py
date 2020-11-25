#from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from alert.middlewares import TokenAuthMiddleware

import chat.routing
import alert.routing

"""

    'websocket' : AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    )
    """

application = ProtocolTypeRouter({
    # vacio por ahora
    'websocket' : TokenAuthMiddleware(
        URLRouter(alert.routing.websocket_urlpatterns)
    )
})