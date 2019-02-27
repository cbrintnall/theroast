from django.views.generic import TemplateView
from django.urls import path, reverse_lazy

from roast.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='roast.html'), name='roast_test'),
    path('create', RoastList.as_view(), name="list"),
    path('detail/<int:pk>', RoastCrud.as_view(), name="list"),
]