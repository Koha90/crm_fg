from django import forms
from django.utils.text import slugify

from .models import Client


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('title', 'city', 'address', 'decision_maker', 'phone',
                  'email', 'first_call', 'description', 'next_call')
