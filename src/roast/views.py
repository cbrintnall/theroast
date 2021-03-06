from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.decorators import action
from rest_framework.response import Response

from roast.utils.gcs_utils import get_image
from roast.models import Roast, RoastImage
from roast.serializers import RoastSerializer, RoastImageSerializer
from io import BytesIO

import base64


class Roasts(viewsets.ModelViewSet):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

class RoastImages(viewsets.ModelViewSet):
    queryset = RoastImage.objects.all()
    serializer_class = RoastImageSerializer
    lookup_field = 'unique_id'
    lookup_value_regex = '([0-9a-f\-]{36}|[0-9a-f]{32})'

    def retrieve(self, request, unique_id=None):
        image = get_image(unique_id)

        if image is None:
            return Response(status=HTTP_404_NOT_FOUND)

        file_bytes = BytesIO()
        image.download_to_file(file_bytes)
        return HttpResponse(file_bytes.getvalue(), content_type="image/jpeg")