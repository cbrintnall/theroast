from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from rest_framework import generics

from roast.models import Roast
from roast.serializers import RoastSerializer

class RoastList(generics.ListCreateAPIView):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

class RoastCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

class RoastCreate(CreateView):
    model = Roast
    fields = ('name', 'color')
    template_name = 'home.html'

# class RoastList(ListView):
#     model = Roast
#     template_name = "roast_list.html"

