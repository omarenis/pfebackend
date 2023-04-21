from django.shortcuts import render
from django.urls import include, path


def home(request, *args, **kwargs):
    return render(request=request, template_name='index.html')


urlpatterns = [
    path('', home),
    path('users/', include('gestionusers.views')),
    path('patients', include('gestionpatient.views')),
    path('patient/', include('formparent.views')),
    path('patient/', include('formteacher.views'))
]
