import enum

from django.db.models import QuerySet
from django.urls import path
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, \
    HTTP_204_NO_CONTENT

from common.views import ViewSet, extract_data_with_validation
from formparent.services import AnxityTroubleParentService, BehaviorTroubleParentService, \
    HyperActivityTroubleParentService, LearningTroubleParentService, FormAbrParentService, \
    SomatisationTroubleParentService

from formteacher.services import BehaviorTroubleTeacherService, \
    HyperActivityTroubleTeacherService, InattentionTroubleTeacherService, FormAbrTeacherService
from gestionusers.services import UserService
from .models import DiagnosticSerializer, ConsultationSerializer, PatientSerializer, SuperviseSerializer
from .service import ConsultationService, DiagnosticService, PatientService, SuperviseService


class Quantify(enum.Enum):
    never = 0
    sometimes = 1
    usual = 2
    always = 3


def add_person(data: dict, type_user: str):
    if data is not None:
        person = UserService().filter_by({'loginNumber': data.get('cin'), 'typeUser': type_user}).first()
        if person is None:
            person = UserService().create(data)
            if isinstance(person, Exception):
                raise person
        return person.id
    return None


def add_other_data_to_patient(data: dict, service, patient_id, teacher_id=None):
    if teacher_id is not None:
        _object = service.filter_by({'teacher_id': teacher_id, 'patient_id': patient_id}).first()
    else:
        _object = service.filter_by({'patient_id': patient_id}).first()
    if _object is not None:
        _object = service.put(data=data, _id=_object.id)
    else:
        data['patient_id'] = patient_id
        if teacher_id is not None:
            data['teacher_id'] = teacher_id
    _object = service.create(data=data)
    if isinstance(_object, Exception):
        print(_object)
        raise _object
    return _object


class PatientViewSet(ViewSet):
    def __init__(self, serializer_class=PatientSerializer, service=PatientService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

    def get_permissions(self):
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        try:
            filter_dictionary = {}
            if request.user.type_user == 'teacher':
                filter_dictionary['form__teacher_id'] = request.user.id
            elif request.user.type_user == 'school':
                filter_dictionary['form__teacher__schoolteacherids__school_id'] = request.user.id
            elif request.user.type_user == 'parent':
                filter_dictionary['parent_id'] = request.user.profile_id
            elif not request.user.profile.is_super_doctor:
                filter_dictionary['supervise__doctor_id'] = request.user.profile_id
                filter_dictionary['supervise__accepted'] = True
            for i in request.query_params:
                filter_dictionary[i] = request.query_params.get(i)

            output = []
            pts = self.service.list().distinct() if list(
                request.GET.keys()) == [] and filter_dictionary == {} else self.service.filter_by(filter_dictionary)
            if isinstance(pts, QuerySet):
                for i in pts.distinct():
                    output.append(self.serializer_class(i).data)
            else:
                for i in pts:
                    patient_private_data, patient_object = i
                    output.append(self.serializer_class(patient_object).data)
            return Response(data=output, status=HTTP_200_OK)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None, *args, **kwargs):
        patient_data = self.service.retrieve(_id=pk)
        if isinstance(patient_data, Exception):
            return Response(data={'error': str(patient_data)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        medical_teacher_data = None
        return Response({**self.serializer_class(patient_data).data,
                         'school': patient_data.form_set.first().teacher.schoolteacherids.school.name},
                        status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = extract_data_with_validation(request=request, fields=self.fields)
        if request.user.type_user == 'parent':
            data['parent_id'] = request.user.id
        if request.user.type_user == 'teacher':
            data['parent_id'] = request.data.get('parent')
            data['teacher_id'] = request.user.id
        try:
            patient_object = self.service.create(data=data, type_user=request.user.type_user)
            return Response(data=self.serializer_class(patient_object).data, status=HTTP_201_CREATED)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None, *args, **kwargs):
        deleted = self.service.delete(pk)
        if isinstance(deleted, Exception):
            return Response(data={'error': str(deleted)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=HTTP_204_NO_CONTENT)


class RenderVousViewSet(ViewSet):
    def get_permissions(self):
        if self.request.user.profile.is_super_doctor == False:
            return [IsAuthenticated()]

    def __init__(self, serializer_class=ConsultationSerializer, service=ConsultationService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class SuperviseViewSet(ViewSet):
    def get_permissions(self):
        if self.request.user.profile.is_super_doctor is True:
            return [IsAuthenticated()]

    def __init__(self, serializer_class=SuperviseSerializer, service=SuperviseService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class DiagnosticViewSet(ViewSet):
    def get_permissions(self):
                if self.request.user.profile.is_super_doctor == False:
                     return [IsAuthenticated()]

    def __init__(self, serializer_class=DiagnosticSerializer, service=DiagnosticService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


patients, patient = PatientViewSet.get_urls()
supervises, supervise = SuperviseViewSet.get_urls()
consultations, consultation = RenderVousViewSet.get_urls()
diagnostics, diagnostic = DiagnosticViewSet.get_urls()

urlpatterns = [
    path('', patients), path('/<int:pk>', patient),
    path('/supervises', supervises),
    path('/supervises/<int:pk>', supervise),
    path('/consultations', consultations),
    path('/consultations/<int:pk>', consultation),
    path('/diagnostics', diagnostics),
    path('/diagnostics/<int:pk>', diagnostic)
]
