from typing import List
from weakref import WeakValueDictionary

from django.db.models import Q, signals
from django.http import StreamingHttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ... import models
from .. import serializers
from .stream import SignalStream


class AnnouncementListAll(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        announcements = models.Announcement.get_all(user=request.user)
        serializer = serializers.AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)


class AnnouncementListMyFeed(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        announcements = request.user.get_feed()
        serializer = serializers.AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)


class AnnouncementChangeStream(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return StreamingHttpResponse(
            SignalStream(
                signal=signals.post_save,
                model=models.Announcement,
                serializer=serializers.AnnouncementSerializer,
            )
        )
