from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from roast.models import Roast
from roast.forms import RoastForm

class RoastCreate(CreateView):
    model = Roast
    # form_class = RoastForm
    fields = ('name', 'color')
    template_name = 'home.html'

class RoastList(ListView):
    model = Roast
    template_name = "roast_list.html"

