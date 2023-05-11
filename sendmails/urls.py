from apps.views import *
from django.urls import path
from sendmails.views import groups, notification, admin_notifications

urlpatterns = [
    path('', groups, name='group'),
    path('notification/', notification, name='notification'),
    path('status/', admin_notifications, name='admin_notifications'),
]