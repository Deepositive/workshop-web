#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2015-12-30 13:08:17
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2015-12-30 16:50:50
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

# Pytest
import pytest

pytestmark = pytest.mark.django_db


def test_api_endpoints(client):
    url = reverse('event-view')
    content = client.get(url)
    assert content.status_code == 200  # GET METHOD
    url = reverse('notification-view')
    content = client.get(url)
    assert content.status_code == 200  # GET METHOD


def test_post_method_not_allowed(client):
    url = reverse('event-view')
    data = {}
    content = client.post(url, data)
    assert content.status_code == 405  # Method Not Allowed

    url = reverse('notification-view')
    data = {}
    content = client.post(url, data)
    assert content.status_code == 405  # Method Not Allowed
