from rest_framework import serializers
from drugs.models import Drugs, Stores


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ('name', 'street_name', 'latitude', 'longitude')


class DrugsSerializer(serializers.ModelSerializer):
    store_rel = StoresSerializer(many=True, read_only=True, source='store')

    class Meta:
        model = Drugs
        fields = ('name', 'price', 'description', 'store_rel')
