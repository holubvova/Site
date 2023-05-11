from django import forms
from django.contrib.auth.models import User
from .models import Group , Notification

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'})
        }

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['Subject', 'message', 'repeatTime','group','active']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'repeatTime': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            # 'active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

