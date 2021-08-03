from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('gestionusers.views')),
    path('messages/', include('chat.views')),
    path('patients', include('gestionpatient.views')),
    path('patient/', include('formparent.views')),
    path('patient/', include('formteacher.views'))
]
