from django import forms
from .models import api


class apiForm(forms.ModelForm):
    class Meta:
        model = api
        fields = ['name', 'Keywords', 'Status', 'uuid', 'location']


