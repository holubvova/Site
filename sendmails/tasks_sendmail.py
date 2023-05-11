from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from Site.celery import app
from sendmails.sendmails import send_maill


@app.task(queue='email')
def task_send_mail(email,message, subject):
    result = send_maill(email,message=message, subject=subject)
    print(result)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_notifications",
        {
            "type": "admin.notification",
            "message": {
                "queue": "email",
                "name": f"{result['name']}",
                "data": f"{result['data']}",
                "recipient" :f"{result['recipient']}",
                "result": f"{result['result']}",
                "timestamp":f"{result['timestamp']}"
            }
        },
    )
    return 0

