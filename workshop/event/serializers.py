#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = ('name_of_the_event', 'photo_of_the_area', 'description_of_the_event',
                  'location', 'name_of_the_contact_person', 'phone_number_of_the_contact_person')


class NotificationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = models.Notification
        fields = ('event', 'notification_text')
