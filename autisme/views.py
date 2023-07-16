from django.urls import path

from autisme.models import Level1serializer, Autistic, ConsultationSerializer, AutisticSerializer
from autisme.services import Level1service, ConsultationService, AutisticService
from common.views import ViewSet
from gestionpatient.models import SuperviseSerializer
from gestionpatient.service import SuperviseService


class AutisticViewSet(ViewSet):
    def __init__(self, serializer_class=AutisticSerializer, service=AutisticService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['parent'] = request.user
        return super().create(request)


class Level1ViewSet(ViewSet):
    def __init__(self, serializer_class=Level1serializer, service=Level1service(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['parent'] = request.user
        return super().create(request, *args)


class ConsultationViewSet(ViewSet):

    def __init__(self, serializer_class=ConsultationSerializer, service=ConsultationService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class SuperviseViewSet(ViewSet):

    def __init__(self, serializer_class=SuperviseSerializer, service=SuperviseService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


autistics, autistic = AutisticViewSet.get_urls()
level1_set, level1 = Level1ViewSet.get_urls()
consultations, consultation = ConsultationViewSet.get_urls()
supervises, supervise = SuperviseViewSet.get_urls()

urlpatterns = [
    path('autistics', autistics),
    path('autistics/<int:pk>', autistic),
    path('level1', level1_set),
    path('level1/<int:pk>', level1),
    path('consultations', consultations),
    path('consultations/<int:pk>', consultation),
    path('supervises', supervises),
    path('supervises/<int:pk>', supervise)
]
