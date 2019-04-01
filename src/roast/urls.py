from django.views.generic import TemplateView
from django.urls import path, reverse_lazy

from roast.views import *

roasts = Roasts.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', TemplateView.as_view(template_name='roast.html'), name='roast_test'),
    path('roast', roasts, name="roasts"),
]