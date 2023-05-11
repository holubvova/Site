from django.urls import re_path
from . import consumers

websocketstatus_urlpatterns = [
    re_path(r'ws/admin_notifications/$', consumers.AdminNotificationsConsumer.as_asgi()),
]