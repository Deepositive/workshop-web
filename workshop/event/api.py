#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import Event, Notification
from .serializers import EventSerializer, NotificationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class EventViewSet(generics.ListAPIView):

    """
    API endpoint that allows user to view Events
    """
    permission_classes = (AllowAny, )
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class NotificationViewSet(generics.ListAPIView):

    """
    API endpoint that allows user to view Events
    """
    permission_classes = (AllowAny, )
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
