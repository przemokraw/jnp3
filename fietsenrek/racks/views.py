from rest_framework import generics

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
