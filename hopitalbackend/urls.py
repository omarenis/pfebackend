from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path


def home(request, *args, **kwargs):
    return render(request=request, template_name='index.html')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('users/', include('gestionusers.views')),
    path('messages/', include('chat.views')),
    path('patients', include('gestionpatient.views')),
    path('patient/', include('formparent.views')),
    path('patient/', include('formteacher.views'))
]
