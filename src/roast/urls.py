from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from roast.views import *

roast_router = DefaultRouter()
roast_router.register(r'', Roasts)

# urlpatterns = [
#     # path('id/<int:pk>', TemplateView.as_view(template_name='roast.html'),
#     path('id/<int:pk>', roast_detail, name='roast_detail'),
#     path('', roasts, name="roasts"),
# ]

urlpatterns = [
    path('', include(roast_router.urls))
]