from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]