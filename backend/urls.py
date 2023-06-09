"""backend URL Configuration

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
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    return HttpResponse(b"hello world")


# @api_view(['DELETE'])
# @permission_classes([IsAdminUser, IsAuthenticated])
# def clear_data(request, *args, **kwargs):
#     try:
#         for i in Patient.objects.all():
#             i.delete()
#         for i in Doctor.objects.all():
#             i.delete()
#         for i in School.objects.all():
#             i.delete()
#         for i in Message.objects.all():
#             i.delete()
#         for i in Parent.objects.all():
#             i.delete()
#         for i in Teacher.objects.all():
#             i.delete()
#         for i in Localisation.objects.all():
#             i.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
#     except Exception as exception:
#         return Response({'message': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


urlpatterns = [
    # path('api/delete_data', clear_data),
    path('api/', home),
    path('api/persons', include('gestionusers.views')),
    path('api/patients', include('gestionpatient.views')),
    path('api/patient/', include('tdah.views')),
    path('api/autisme/', include('autisme.views')),
    # path('api/messages', include('chat.views'))
]
