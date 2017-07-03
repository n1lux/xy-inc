from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from xyinc.api.models import Poi


class PoiSerializer(ModelSerializer):

    class Meta:
        model = Poi
        fields = ('name', 'x', 'y')

    def create(self, validated_data):
        poi = Poi.create(**validated_data)
        poi.save()
        return poi