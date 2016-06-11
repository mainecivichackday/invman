from django.contrib import admin
from django import forms
from .models import api

class apiAdminForm(forms.ModelForm):

    class Meta:
        model = api
        fields = '__all__'


class apiAdmin(admin.ModelAdmin):
    form = apiAdminForm
    list_display = ['name', 'created', 'last_updated', 'Keywords', 'Status', 'uuid', 'location']
    readonly_fields = ['name', 'created', 'last_updated', 'Keywords', 'Status', 'uuid', 'location']

admin.site.register(api, apiAdmin)


