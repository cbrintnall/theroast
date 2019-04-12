from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

from roast.views import *

roast_router = SimpleRouter()
roast_router.register(r'', Roasts)

roast_image_router = SimpleRouter()
roast_image_router.register(r'', RoastImages)

urlpatterns = [
    path('', include(roast_router.urls)),
    path('images/', include(roast_image_router.urls))
]