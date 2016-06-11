from django.core.urlresolvers import reverse
from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class api(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Keywords = models.TextField(max_length=65535)
    Status = models.TextField(max_length=255)
    uuid = models.TextField(max_length=100)
    location = models.TextField(max_length=255)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('api_invman_api_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('api_invman_api_update', args=(self.id,))


