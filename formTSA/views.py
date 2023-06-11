from django.shortcuts import render
from django.urls import path

from common.views import ViewSet
from formTSA.models import level1Serializer,level2Serializer
from formTSA.services import level1Service,level2Service



class level1ViewSet(ViewSet):
    def __init__(self, serializer_class=level1Serializer, service=level1Service(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

class level2ViewSet(ViewSet):
    def __init__(self, serializer_class=level2Serializer, service=level2Service(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)



level1_list, level1_object = level1ViewSet.get_urls()
level2_list, level2_object = level2ViewSet.get_urls()


urlpatterns = [
    path('level1_list', level1_list),
    path('level1_list/<int:id>', level1_object),
    path('level2_list', level2_list),
    path('level2_list/<int:id>', level2_object),
]