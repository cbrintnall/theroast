from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('user', TemplateView.as_view(template_name='home.html'), name="home"),
    path('r/<unique_id>', TemplateView.as_view(template_name='roast.html'), name='r')
]