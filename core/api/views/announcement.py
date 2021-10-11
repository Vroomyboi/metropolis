from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ... import models
from .. import serializers


class AnnouncementListAll(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        announcements = models.Announcement.get_all(user=request.user)
        serializer = serializers.AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)


class AnnouncementListMyFeed(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ["me_ann"]

    def get(self, request, format=None):
        announcements = request.user.get_feed()
        serializer = serializers.AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)
