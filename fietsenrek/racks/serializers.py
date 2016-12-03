from rest_framework import serializers

from . import models


class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rack
        fields = '__all__'
