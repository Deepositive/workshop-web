#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from versatileimagefield.fields import VersatileImageField
from uuid_upload_path import upload_to


class Event(models.Model):
    name_of_the_event = models.CharField(
        blank=False, null=False, max_length=256)
    photo_of_the_area = VersatileImageField(
        blank=True, null=True, upload_to=upload_to)
    description_of_the_event = models.CharField(blank=False, null=False,
                                                max_length=100, help_text='Description of the Event')
    duration_of_the_event = models.CharField(blank=True, null=False,
                                             max_length=1000, help_text='Duration in days')
    timings = models.CharField(blank=True, null=False,
                               max_length=1000, help_text='Timing of the event')
    location = models.CharField(blank=False, null=False, max_length=256)
    name_of_the_contact_person = models.CharField(
        blank=False, null=False, max_length=256)
    phone_number_of_the_contact_person = models.CharField(blank=False, null=False,
                                                          max_length=100,
                                                          help_text='Phone Number of the Contact Person')

    def __str__(self):
        return self.name_of_the_event

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-name_of_the_event']


class Notification(models.Model):
    event = models.ForeignKey(Event)
    notification_text = models.CharField(blank=False, null=False,
                                         max_length=10000, help_text='Notification Text')

    def __str__(self):
        return self.event.name_of_the_event

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-event']
