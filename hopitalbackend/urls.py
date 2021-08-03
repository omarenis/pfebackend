"""hopitalbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.shortcuts import render
from django.urls import include, path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


def index_page(request, *args, **kwargs):
    return render(request=request, template_name='hospitalbackend/index.html')


urlpatterns = [
    path('', index_page),
    path('admin/', admin.site.urls),
    path('users/', include('gestionusers.views')),
    path('messages/', include('chat.views')),
    path('patients', include('gestionpatient.views')),
    path('patient/', include('formparent.views')),
    path('patient/', include('formteacher.views'))
]
