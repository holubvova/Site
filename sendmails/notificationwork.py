import datetime
from django.core.mail import send_mass_mail
from Site.settings import EMAIL_HOST_USER
from sendmails.models import Notification


def send_notification_1h():
    obj = scheduler('1h')
    result = obj.get_from_database()
    return result


def send_notification_3h():
    obj = scheduler('3h')
    result = obj.get_from_database()
    return result


def send_notification_12h():
    obj = scheduler('12h')
    result = obj.get_from_database()
    return result


class scheduler:

    def __init__(self, time):
        self.time = time
        self.subject = ""
        self.message = ""
        self.from_email = "hm1haha1hm@gmail.com"
        self.status = ""

    def get_from_database(self):
        notification = list(Notification.objects.filter(repeatTime=self.time))
        print(notification)
        group_recipients1 = None
        for i in notification:
            group_users = list(i.group.members.all())
            group_recipients = [user.email for user in group_users]
            print(group_recipients)
            group_recipients1 = group_recipients
            self.subject = i.Subject
            self.message = i.message
            self.from_email = EMAIL_HOST_USER
            message = (self.subject, self.message, self.from_email, group_recipients)
            try:
                send_mass_mail((message,), fail_silently=False)
                self.status = "success"

            except:
                print("error")
                self.status = "error"

        return {
            "queue": "long_task",
            "recipient": f"{group_recipients1}",
            "name": f"{self.subject}",
            "data": f"{self.message}",
            "result": f"{self.status}",
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
