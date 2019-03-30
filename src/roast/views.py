from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from rest_framework import generics

from roast.models import Roast
from roast.serializers import RoastSerializer

class RoastPage(TemplateView):
    template_name = "roast_page.html"

    def get_context_data(self, pk, *args, **kwargs):
        context = super(RoastPage, self).get_context_data(*args, **kwargs)
        context["pk"] = pk
        return context

class RoastList(generics.ListCreateAPIView):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

class RoastCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

# class RoastList(ListView):
#     model = Roast
#     template_name = "roast_list.html"

