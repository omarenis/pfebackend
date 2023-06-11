import enum

from django.db.models import QuerySet, Q
from django.urls import path
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, \
    HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from common.views import ViewSet, extract_data_with_validation

from formparent.models import AnxityTroubleParent, FormAbrParent, BehaviorTroubleParent, SomatisationTroubleParent, \
    LearningTroubleParent, HyperActivityTroubleParent, \
    FormAbrParentSerializer, AnxityTroubleParentSerializer, BehaviorTroubleParentSerializer, \
    SomatisationTroubleParentSerializer, LearningTroubleParentSerializer, HyperActivityTroubleParentSerializer
from formteacher.models import FormAbrTeacher, BehaviorTroubleTeacher, InattentionTroubleTeacher, \
    HyperActivityTroubleTeacher, HyperActivityTroubleTeacherSerializer, InattentionTroubleTeacherSerializer, \
    BehaviorTroubleTeacherSerializer, FormAbrSerializer

from gestionusers.models import User, UserSerializer, PersonProfile, Localisation
from gestionusers.services import UserService
from .models import DiagnosticSerializer, ConsultationSerializer, PatientSerializer, SuperviseSerializer, Patient, \
    Consultation
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
            patients = None
            if request.user.profile.is_super_doctor:
                patients = Patient.objects.filter(score_teacher__gt=0, score_parent__gt=0).filter(
                    Q(score_teacher__gte=70) | Q(score_parent__gte=70))

            if request.user.type_user == 'teacher':
                filter_dictionary['teacher_id'] = request.user.id
            elif request.user.type_user == 'school':
                filter_dictionary['teacher__profile__school__id'] = request.user.id
            elif request.user.type_user == 'parent':
                filter_dictionary['parent_id'] = request.user.id
            elif not request.user.profile.is_super_doctor:
                filter_dictionary['supervise__doctor_id'] = request.user.id

            for i in request.query_params:
                filter_dictionary[i] = request.query_params.get(i)

            output = []
            if patients is not None:
                pts = patients.distinct() if list(
                    request.GET.keys()) == [] and filter_dictionary == {} else patients.filter(**filter_dictionary)
            else:
                pts = Patient.objects.filter(**filter_dictionary)

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

        return Response({**self.serializer_class(patient_data).data},
                        status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = extract_data_with_validation(request=request, fields=self.fields)
        try:
            parent_id = None
            teacher_id = None

            if request.user.type_user == 'parent':
                parent_id = request.user.id
            elif request.user.type_user == 'teacher':
                parent_cin = data.get('parent')
                if parent_cin is not None:
                    parent = user_service.get_by({'login_number': parent_cin})
                    if parent is not None:
                        parent_id = parent.id
                    else:
                        pr = PersonProfile(family_name='inactive', is_super_doctor=None)
                        pr.save()
                        parent = User(login_number=parent_cin, username=parent_cin, name=parent_cin, profile=pr,
                                      is_active=False)
                        parent.save()
                        parent_id = parent.id

                teacher_id = request.user.id

            data['parent'] = parent_id
            data['teacher'] = teacher_id

            patient_object = self.service.create(data=data, type_user=request.user.type_user)
            return Response(data=self.serializer_class(patient_object).data, status=HTTP_201_CREATED)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None, *args, **kwargs):
        deleted = self.service.delete(pk)
        if isinstance(deleted, Exception):
            return Response(data={'error': str(deleted)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=HTTP_204_NO_CONTENT)

    def update(self, request, pk=None, *args, **kwargs):
        request.data['type_user'] = self.request.user.type_user

        if self.request.user.type_user == "teacher":
            request.data['teacher'] = self.request.user.id

        return super().update(request=request, pk=pk, *args, **kwargs)


class RenderVousViewSet(ViewSet):
    def get_permissions(self):
        if not self.request.user.profile.is_super_doctor:
            return [IsAuthenticated()]

    def __init__(self, serializer_class=ConsultationSerializer, service=ConsultationService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

    def create(self, request, *args, **kwargs):
        data = extract_data_with_validation(request=request, fields=self.fields)
        try:
            data['doctor'] = request.user.id
            supervise_object = self.service.create(data=data)
            return Response(data=self.serializer_class(supervise_object).data, status=HTTP_201_CREATED)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        user = request.user

        if user.type_user == 'doctor' and user.profile.is_super_doctor == False:

            consultations = Consultation.objects.filter(doctor=user.id)
        elif user.type_user == 'parent':
            consultations = Consultation.objects.filter(patient__parent_id=user.id)
        else:
            return Response(data={'error': 'Invalid user type'}, status=HTTP_400_BAD_REQUEST)

        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class SuperviseViewSet(ViewSet):
    def get_permissions(self):
        if self.request.user.profile.is_super_doctor:
            return [IsAuthenticated()]

    def __init__(self, serializer_class=SuperviseSerializer, service=SuperviseService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class DiagnosticViewSet(ViewSet):
    def get_permissions(self):
        if not self.request.user.profile.is_super_doctor:
            return [IsAuthenticated()]

    def __init__(self, serializer_class=DiagnosticSerializer, service=DiagnosticService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


user_service = UserService()
pat_service = PatientService()


@api_view(['GET'])
def find(request, pk=None):
    parent = user_service.get_by({'login_number': pk})
    if parent:
        patients = pat_service.filter_by({'parent_id': parent.id, 'score_teacher': 0})
        parent_serializer = UserSerializer(parent)
        patients_serializer = PatientSerializer(patients, many=True)
        return Response({'parent': parent_serializer.data, 'patients': patients_serializer.data})
    else:
        return Response({'message': 'Parent not found'}, status=HTTP_404_NOT_FOUND)


@api_view(['GET'])
def patscore(request, pk=None):
    p = PatientSerializer(Patient.objects.get(id=pk))
    x1 = FormAbrParentSerializer(FormAbrParent.objects.get(patient_id=pk))
    x2 = BehaviorTroubleParentSerializer(BehaviorTroubleParent.objects.get(patient_id=pk))
    x3 = LearningTroubleParentSerializer(LearningTroubleParent.objects.get(patient_id=pk))
    x4 = SomatisationTroubleParentSerializer(SomatisationTroubleParent.objects.get(patient_id=pk))
    x5 = HyperActivityTroubleParentSerializer(HyperActivityTroubleParent.objects.get(patient_id=pk))
    x6 = AnxityTroubleParentSerializer(AnxityTroubleParent.objects.get(patient_id=pk))

    x7 = BehaviorTroubleTeacherSerializer(BehaviorTroubleTeacher.objects.get(patient_id=pk))
    x8 = HyperActivityTroubleTeacherSerializer(HyperActivityTroubleTeacher.objects.get(patient_id=pk))
    x9 = InattentionTroubleTeacherSerializer(InattentionTroubleTeacher.objects.get(patient_id=pk))
    x10 = FormAbrSerializer(FormAbrTeacher.objects.get(patient_id=pk))

    return Response({
        "Patient": p.data,
        "FormAbrParent": x1.data,
        "BehaviorTroubleParent": x2.data,
        "LearningTroubleParent": x3.data,
        "SomatisationTroubleParent": x4.data,
        "HyperActivityTroubleParent": x5.data,
        "AnxityTroubleParent": x6.data,

        "BehaviorTroubleTeacher": x7.data,
        "InattentionTroubleTeacher": x8.data,
        "HyperActivityTroubleTeacher": x9.data,
        "FormAbrTeacher": x10.data
    })


@api_view(['GET'])
def dashboard(request):
    data = {
        "total": Patient.objects.count(),
        "males": Patient.objects.filter(gender="M").count(),
        "females": Patient.objects.filter(gender="F").count(),
        "supervised": Patient.objects.filter(is_supervised=True).count(),
        "supervisedmales": Patient.objects.filter(is_supervised=True, gender="M").count(),
        "supervisedfemales": Patient.objects.filter(is_supervised=True, gender="F").count(),
        "consulted": Patient.objects.filter(is_consulted=True).count(),

        ">70": Patient.objects.filter(score_teacher__gt=0, score_parent__gt=0).filter(
            Q(score_teacher__gte=70) | Q(score_parent__gte=70)).count(),
        "waiting for parent": Patient.objects.filter(score_teacher__gt=0, score_parent=0).count(),
        "waiting for teacher": Patient.objects.filter(score_teacher=0, score_parent__gt=0).count(),

    }
    return Response(data)


patients, patient = PatientViewSet.get_urls()
supervises, supervise = SuperviseViewSet.get_urls()
consultations, consultation = RenderVousViewSet.get_urls()
diagnostics, diagnostic = DiagnosticViewSet.get_urls()

urlpatterns = [
    path('/find/<pk>', find),
    path('/details/<int:pk>', patscore),
    path('/dashboard', dashboard),
    path('', patients), path('/<int:pk>', patient),
    path('/supervises', supervises),
    path('/supervises/<int:pk>', supervise),
    path('/consultations', consultations),
    path('/consultations/<int:pk>', consultation),
    path('/diagnostics', diagnostics),
    path('/diagnostics/<int:pk>', diagnostic)
]
