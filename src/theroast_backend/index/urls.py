from django.urls import path
from index.views import test

urlpatterns = [
    path('', test)
]