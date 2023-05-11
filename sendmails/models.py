from django.db import models

from apps.models import User

REPEAT_TIME = [
    ('1h', '1h'),
    ('3h', '3h'),
    ('12h', '12h'),
]

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Notification(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    repeatTime = models.CharField(verbose_name='repeatTime',max_length=5 ,choices=REPEAT_TIME,default='1h')

    def __str__(self):
        return f'{self.message, self.group}'