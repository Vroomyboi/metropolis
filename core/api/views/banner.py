import json

from django.http import StreamingHttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from ... import models
from .. import serializers


class Banner(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        if not hasattr(settings, 'BANNER_SHOW'):
            return Response(status=500)
        if not settings.BANNER_SHOW:
            return Response(status=404)
        return Response({
            'text': settings.BANNER_TEXT,
            'btn': {
                'url': settings.BANNER_URL,
                'text': settings.BANNER_URL_TEXT,
            },
            **({
                'timeframe': {
                    'start': settings.BANNER_SHOW_START,
                    'end': settings.BANNER_SHOW_END,
                },
            } if hasattr(settings, 'BANNER_SHOW_START') else {}),
        })
