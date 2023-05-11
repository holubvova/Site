import time

from django.shortcuts import render

from .models import Group
from .forms import GroupForm , NotificationForm
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def groups(request):
    groups = Group.objects.all()
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = GroupForm()
    context = {
        'groups': groups,
        'form': form,
    }
    return render(request, 'apps/groups.html', context)

def notification(request):
    groups = Group.objects.all()
    form = NotificationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotificationForm()
    context = {
        'groups': groups,
        'form': form,
    }
    return render(request, 'apps/notification.html', context)






def admin_notifications(request):
    return render(request, 'sendmails/admin_notifications.html')