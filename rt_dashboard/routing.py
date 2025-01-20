from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from dashboard import consumer as dashboard_consumer

from django.urls import path

websocket_urlPatterns = [
    path('ws/dashboard-analytics', dashboard_consumer.DashboardAnalytics)
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPatterns))
});