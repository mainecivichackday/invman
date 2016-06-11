import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import api
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_api(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["Keywords"] = "Keywords"
    defaults["Status"] = "Status"
    defaults["uuid"] = "uuid"
    defaults["location"] = "location"
    defaults.update(**kwargs)
    return api.objects.create(**defaults)


class apiViewTest(unittest.TestCase):
    '''
    Tests for api
    '''
    def setUp(self):
        self.client = Client()

    def test_list_api(self):
        url = reverse('api_invman_api_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_api(self):
        url = reverse('api_invman_api_create')
        data = {
            "name": "name",
            "Keywords": "Keywords",
            "Status": "Status",
            "uuid": "uuid",
            "location": "location",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_api(self):
        api = create_api()
        url = reverse('api_invman_api_detail', args=[api.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_api(self):
        api = create_api()
        data = {
            "name": "name",
            "Keywords": "Keywords",
            "Status": "Status",
            "uuid": "uuid",
            "location": "location",
        }
        url = reverse('api_invman_api_update', args=[api.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


