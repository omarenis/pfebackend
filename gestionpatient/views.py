from django.urls import path

from common.models import text_field
from common.repositories import Repository
from common.services import Service
from common.views import ViewSet
from formparent.services import AnxityTroubleParentService, ImpulsivityTroubleParentService, \
    LearningTroubleParentService, SomatisationTroubleParentService
from gestionpatient.models import Orientation, OrientationSerializer, Patient, PatientSerializer

PATIENT_FIELDS = {
    'block': text_field,
    'name': text_field,
    'family_name': text_field,
    'parent_full_name': text_field,
    'birthdate': {'type': 'date', 'required': True},
    'parent_id': {'type': 'foerign_key', 'required': False},
    'doctor_id': {'type': 'foreign_key', 'required': False}
}

ORIENTATION_FIELDS = {
    'patient_id': {'type': 'foerign_key', 'required': True},
    'doctor_id': {'type': 'foreign_key', 'required': True},
    'diagnostic': text_field
}


class PatientRepository(Repository):
    def __init__(self, model=Patient):
        super().__init__(model)


class OrientationRepository(Repository):
    def __init__(self, model=Orientation):
        super().__init__(model)


class PatientService(Service):
    def __init__(self, repository=PatientRepository()):
        super().__init__(repository)


class OrientationService(Service):
    def __init__(self, repository=OrientationRepository()):
        super().__init__(repository)


class PatientViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=PatientSerializer, service=PatientService(), **kwargs):
        if fields is None:
            fields = PATIENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)
        self.anxity_trouble_parent_service = AnxityTroubleParentService()
        self.impulsivity_trouble_parent_service = ImpulsivityTroubleParentService()
        self.learning_trouble_parent_service = LearningTroubleParentService()
        self.somatisation_trouble_parent_service = SomatisationTroubleParentService()

    def create(self, request, *args, **kwargs):
        data = {}
        for i in list(self.fields.keys()):
            data[i] = request.data.get(i)
        patient_object = self.service.filter_by(data=data).first()
        if patient_object is None:
            patient_object = self.service.create(data)
        patient_id = patient_object.id


class OrientationViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=OrientationSerializer, service=OrientationService(), **kwargs):
        if fields is None:
            fields = ORIENTATION_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


patients = PatientViewSet.as_view({'get': 'list', 'post': 'create'})

patient = PatientViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

orientations = OrientationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

orientation = OrientationViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

urlpatterns = [
    path('', patients),
    path('<int:id>', patient),
    path('orientations', orientations),
    path('orentations/<int:id>', orientation)
]
