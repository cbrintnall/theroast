from rest_framework import serializers
from roast.models import Roast

class RoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roast
        fields = ('id', 'name', 'color')