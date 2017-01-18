from django.core.cache import cache
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

    def get_queryset(self):
        queryset = cache.get('racks:all')
        if not queryset:
            queryset = models.Rack.objects.select_related().all()
            cache.set('racks:all', queryset, timeout=60 * 1)
        return queryset


class RackTopListView(generics.ListAPIView):
    serializer_class = serializers.RackSerializer

    def get_queryset(self):
        queryset = cache.get('racks:top')
        if not queryset:
            queryset = models.Rack.objects.select_related().all().order_by('-vote')[:10]
            cache.set('racks:top', queryset, timeout=60 * 5)
        return queryset


class RackDetailViewMixin(object):
    def get_object(self):
        pk = self.kwargs.get('pk')
        rack = cache.get('racks:{}'.format(pk))
        if not rack:
            rack = get_object_or_404(models.Rack, pk=pk)
        return rack


class RackUpVoteView(RackDetailViewMixin, generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack.up_vote()
        return super().patch(request, *args, **kwargs)


class RackDownVoteView(RackDetailViewMixin, generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack.down_vote()
        return super().patch(request, *args, **kwargs)


class RackSolveView(RackDetailViewMixin, generics.UpdateAPIView):
    serializer_class = serializers.RackSerializer

    def patch(self, request, *args, **kwargs):
        rack = self.get_object()
        rack.solve()
        return super().patch(request, *args, **kwargs)


class RackDescriptionSearchView(generics.ListAPIView):
    serializer_class = serializers.RackSerializer

    def get_queryset(self):
        text = self.request.query_params.get('text', '')
        return models.Rack.objects.filter(description__search=text)


class RackProblems(views.APIView):
    def get(self, request):
        return Response(data=models.RackProblems.CHOICES,
                        status=status.HTTP_200_OK)
