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


class RackVoteView(views.APIView):
    def patch(self, request):
        rack_id = request.data['rack_id']
        rack = models.Rack.objects.filter(id=rack_id)
        vote = int(request.data['vote'])

        if rack.count() != 1 or vote not in (1, -1):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        rack = rack[0]
        rack = rack.up_vote() if vote > 0 else rack.down_vote()
        return Response({'rack': serializers.RackSerializer(instance=rack)},
                        status=status.HTTP_200_OK)
