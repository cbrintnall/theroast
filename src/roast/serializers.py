from rest_framework import serializers
from roast.models import Roast, RoastImage
from roast.utils.gcs_utils import upload_b64

class RoastImageSerializer(serializers.ModelSerializer):
    content = serializers.CharField(write_only=True)
    unique_id = serializers.CharField(read_only=True)

    def create(self, data):
        content = data.get('content')
        path = upload_b64(content)
        return RoastImage.objects.create(path=path)

    class Meta:
        model = RoastImage
        fields = ('content', 'unique_id')

class RoastSerializer(serializers.ModelSerializer):
    images = RoastImageSerializer(many=True)
    ready = serializers.BooleanField(read_only=True)

    def create(self, data):
        images, instances = data.pop('images'), []
        serializer = RoastImageSerializer()

        for image in images:
            image = serializer.create(image)
            image.save()
            instances.append(image)

        roast = Roast(**data)
        roast.save()

        roast.images.add(*instances)
        roast.save()

        return roast

    class Meta:
        model = Roast
        fields = '__all__'