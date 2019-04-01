from rest_framework import serializers
from roast.models import Roast, RoastImage

import base64

class RoastImageSerializer(serializers.ModelSerializer):
    def create(self, data):
        print(data)

    class Meta:
        model = RoastImage
        fields = '__all__'

class RoastSerializer(serializers.ModelSerializer):
    images = RoastImageSerializer(many=True)

    def create(self, data):
        image = RoastImage()
        return super(RoastSerializer, self).create(data)

    class Meta:
        model = Roast
        fields = '__all__'