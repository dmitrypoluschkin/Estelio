from django.core import serializers

from stores.models import Stores, Cities
from rest_framework import serializers


class StoresSerializer(serializers.Serializer):

    class Meta:
        model = Stores
        field = ('title', 'long', 'lat', 'address', 'phone', 'email', 'website', 'city')


class CitiesSerializer(serializers.Serializer):
    stores = StoresSerializer(source="stores_set", many=True)

    class Meta:
        model = Cities
        fields = ('title', 'long', 'lat', 'stores')






