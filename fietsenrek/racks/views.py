from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

from . import serializers
from . import models


class RackCreateView(generics.CreateAPIView):
    serializer_class = serializers.RackSerializer


class RackListView(generics.ListAPIView):
    serializer_class = serializers.RackSerializer
    queryset = models.Rack.objects.all()


class RackTopListView(generics.ListAPIView):
    serializer_class = serializers.RackSerializer
    queryset = models.Rack.objects.all().order_by('-vote')[:10]


class RackUpVoteView(generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer
    queryset = models.Rack.objects.all()

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack.up_vote()
        return super().patch(request, *args, **kwargs)


class RackDownVoteView(generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer
    queryset = models.Rack.objects.all()

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack = rack.down_vote()
        return super().patch(request, *args, **kwargs)


class RackSolveView(generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer
    queryset = models.Rack.objects.all()

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack.solve()
        return super().patch(request, *args, **kwargs)
