from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from rest_framework import viewsets

from roast.models import Roast
from roast.serializers import RoastSerializer

class Roasts(viewsets.ModelViewSet):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer
