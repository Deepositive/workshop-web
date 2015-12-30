#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Event, Notification


class EventAdmin(admin.ModelAdmin):

    '''
    Admin View for Event
    '''
    list_display = ('name_of_the_event', 'photo_of_the_area', 'description_of_the_event',
                    'location', 'name_of_the_contact_person', 'phone_number_of_the_contact_person')
    list_filter = ('name_of_the_event', )
    search_fields = ['name_of_the_event', 'photo_of_the_area', 'description_of_the_event',
                     'location', 'name_of_the_contact_person', 'phone_number_of_the_contact_person', ]

    def photo_of_the_area(self, obj):
        if obj.photo:
            return '<img src="%s"/>' % obj.photo.thumbnail['100x100'].url
        return '(None)'
    photo_of_the_area.allow_tags = True


admin.site.register(Event, EventAdmin)


class NotificationAdmin(admin.ModelAdmin):

    '''
    Admin View for NotificationAdmin
    '''
    list_display = ('event', 'notification_text')
    list_filter = ('event', 'notification_text')
    search_fields = ['event', 'notification_text']

admin.site.register(Notification, NotificationAdmin)
