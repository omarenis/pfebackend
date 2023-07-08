from django.urls import path

from autisme.models import AutisteSerializer, Level1serializer, Autiste, SuperviseSerializer, ConsultationSerializer
from autisme.services import AutisteService, Level1service, SuperviseService, ConsultationService
from common.views import ViewSet


class AutisteViewSet(ViewSet):
    def __init__(self, serializer_class=AutisteSerializer, service=AutisteService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['parent'] = request.user
        return super().create(request)


class Level1viewset(ViewSet):
    def __init__(self, serializer_class=Level1serializer, service=Level1service(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['parent'] = request.user
        request.data['patient'] = Autiste.objects.get(id=int(request.data.get('patient')))
        return super().create(request, *args)


class SuperviseViewSet(ViewSet):

    def __init__(self, serializer_class=SuperviseSerializer, service=SuperviseService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class ConsultationViewSet(ViewSet):

    def __init__(self, serializer_class=ConsultationSerializer, service=ConsultationService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


autistes, autiste = AutisteViewSet.get_urls()
level1_set, level1 = Level1viewset.get_urls()
supervices, supervice = SuperviseViewSet.get_urls()
consultations, consultation = ConsultationViewSet.get_urls()

urlpatterns = [
    path('autistes', autistes),
    path('autistes/<int:pk>', autiste),
    path('level1', level1_set),
    path('level1/<int:pk>', level1),
    path('supervices', supervices),
    path('supervices/<int:pl>', supervice),
    path('consultations', consultations),
    path('consultations/<int:pl>', consultation)
]
