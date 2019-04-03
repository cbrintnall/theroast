from rest_framework import serializers
from roast.models import Roast, RoastImage
from roast.utils.gcs_utils import upload_b64

class RoastImageSerializer(serializers.ModelSerializer):
    # Takes in base64 data to 
    # ingest to google cloud storage
    def create(self, data):
        path = upload_b64(data)
        print(path)

    class Meta:
        model = RoastImage
        fields = '__all__'

class RoastSerializer(serializers.ModelSerializer):
    # for taking in a base64 image from frontend
    images = serializers.ListField(child=serializers.ImageField(), min_length=1)

    def create(self, data):
        # TODO: Figure out another way to get image 
        # information from frontend
        images_values = data.pop("images")
        images = []
        serializer = RoastImageSerializer()

        # Create all images via serializer
        for image in images_values.split("*"):
            print("--------------------------------------------------------------")
            print("--------------------------------------------------------------")
            print(image)
            images.append(serializer.create(image))

        roast = super(RoastSerializer, self).create(data) 
        
        # Add images as foreign keys to the roast.
        for image in images:
            pass

        return 

    class Meta:
        model = Roast
        fields = '__all__'