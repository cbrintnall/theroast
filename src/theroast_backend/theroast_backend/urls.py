"""theroast_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings

def user_logout(request):
    logout(request)
    return redirect('/')

urlpatterns = [
    path('', include(('index.urls', 'index'), namespace="index")),
    path('auth/logout', user_logout, name="logout"),
    path('auth/', include('social_django.urls', namespace='social')),
    path('roast/', include(('roast.urls', 'roast'), namespace='roast')),
    path('admin/', admin.site.urls),
]
