from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from Site.celery import app
from .notificationwork  import *

@app.task(queue='long_task')
def sendmail_1h():
    result = send_notification_1h()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_notifications",
        {
            "type": "admin.notification",
            "message": {
                "queue": "long_task",
                "name": f"{result['name']}",
                "data": f"{result['data']}",
                "recipient" :f"{result['recipient']}",
                "result": f"{result['result']}",
                "timestamp":f"{result['timestamp']}"
            }
        },
    )
    return 0


@app.task(queue='long_task')
def sendmail_3h():
    result = send_notification_3h()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_notifications",
        {
            "type": "admin.notifications",
            "message": {
                "name": f"{result['name']}",
                "data": f"{result['data']}",
                "result": f"{result['result']}",
                "timestamp": f"{result['timestamp']}"
            }
        },
    )
    return 0


@app.task(queue='long_task')
def sendmail_12h():
    result = send_notification_12h()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_notifications",
        {
            "type": "admin.notification",
            "message": {
                "name": f"{result['name']}",
                "data": f"{result['data']}",
                "result": f"{result['result']}",
                "timestamp": f"{result['timestamp']}"
            }
        },
    )
    return 0
