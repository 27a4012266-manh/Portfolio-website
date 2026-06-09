from django import forms
from .models import *

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
