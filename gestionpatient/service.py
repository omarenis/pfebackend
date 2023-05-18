from common.repositories import Repository
from common.services import Service, calculate_score
from formparent.models import BehaviorTroubleParent, LearningTroubleParent, SomatisationTroubleParent, \
    HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent

from formteacher.models import BehaviorTroubleTeacher, HyperActivityTroubleTeacher, InattentionTroubleTeacher, \
    FormAbrTeacher
from gestionusers.models import PersonProfile, User
from gestionusers.services import UserService
from .matrices import matrix
from .models import Consultation, Diagnostic, Patient, Supervise
from datetime import date

URL = "http://localhost:5000/"
APPLICATION_TYPE = "application/json"

global behavior_trouble_parent, learning_trouble_parent, somatisation_trouble_parent, \
    hyperactivity_trouble_parent, form_abr_parent, behavior_trouble_teacher, hyperactivity_trouble_teacher, \
    inattention_trouble_teacher, form_abr_teacher, anxity_trouble_parent

PATIENT_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'family_name': {'type': 'text', 'required': True},
    'birthdate': {'type': 'date', 'required': True},
    'gender': {'type': 'text', 'required': True},
    'parent': {'type': 'foreign_key', 'required': False},
    'teacher': {'type': 'foreign_key', 'required': False},
    'sick': {'type': 'bool', 'required': False},
    'behaviortroubleparent': {'type': 'BehaviorTroubleParent', 'required': False},
    'learningtroubleparent': {'type': 'LearningTroubleParent', 'required': False},
    'somatisationtroubleparent': {'type': 'SomatisationTroubleParent', 'required': False},
    'hyperactivitytroubleparent': {'type': 'HyperActivityTroubleParent', 'required': False},
    'anxitytroubleparent': {'type': 'AnxityTroubleParent', 'required': False},
    'formabrparent': {'type': 'FormAbrParent', 'required': False},
    'behaviortroubleteacher': {'type': 'BehaviorTroubleTeacher', 'required': False},
    'hyperactivitytroubleteacher': {'type': 'HyperActivityTroubleTeacher', 'required': False},
    'inattentiontroubleteacher': {'type': 'InattentionTroubleTeacher', 'required': False},
    'formabrteacher': {'type': 'FormAbrTeacher', 'required': False}
}

SUPERVICE_FIELDS = {
    'patient': {'type': 'one_to_one', 'required': True},
    'doctor': {'type': 'foreign_key', 'required': True}
    
}

CONSULTATION_FIELDS = {
    'doctor': {'type': 'foreign_key', 'required': True},
    'parent': {'type': 'foreign_key', 'required': True},
    'date': {'type': 'int', 'required': True},
    'accepted': {'type': 'bool', 'required': True}
}
DIAGNOSTIC_FIELDS = {
    'patient': {'type': 'foreign_key', 'required': True},
    'diagnostic': {'type': 'str', 'required': True},
    'consultation': {'type': 'foreign_key', 'required': True}
}


def get_fields(type_user):
    return [
        {
            'name': 'behaviortroubleparent',
            '_class': BehaviorTroubleParent,
        },
        {
            'name': 'learningtroubleparent',
            '_class': LearningTroubleParent,
        },
        {
            'name': 'somatisationtroubleparent',
            '_class': SomatisationTroubleParent
        },
        {
            'name': 'hyperactivitytroubleparent',
            '_class': HyperActivityTroubleParent
        },
        {
            'name': 'anxitytroubleparent',
            '_class': AnxityTroubleParent
        },
        {
            'name': 'formabrparent',
            '_class': FormAbrParent
        }
    ] if type_user == 'parent' else [
        {
            'name': 'behaviortroubleteacher',
            '_class': BehaviorTroubleTeacher
        },
        {
            'name': 'hyperactivitytroubleteacher',
            '_class': HyperActivityTroubleTeacher
        },
        {
            'name': 'inattentiontroubleteacher',
            '_class': InattentionTroubleTeacher
        },
        {
            'name': 'formabrteacher',
            '_class': FormAbrTeacher
        }
    ]


def get_age(birthdate):
    print(date.today())
    return (date.today() - birthdate).total_seconds() // (3600 * 24 * 365)


def get_score(gender, data, birthdate, class_name, type_user):
    return matrix(gender=gender, type_user=type_user,
                  tranche=int(get_age(birthdate=birthdate) // 3))[class_name][calculate_score(data)]


def save_or_update_instance_form(instance, field, _class, values: dict):
    if hasattr(instance, field):
        print(getattr(instance, field))
        _object = getattr(instance, field)
        if _object is not None:
            for key, value in values.items():
                setattr(_object, key, value)
    else:
        _object = _class(**values)
    setattr(_object, 'patient', instance)
    _object.save()


def save_instance_form(patient, field, _class, values):
    setattr(patient, field, _class(**values))
    getattr(patient, field).save()


def save_instances_form(instances: list):
    for instance in instances:
        save_or_update_instance_form(instance=instance['instance'], _class=instance['_class'],
                                     values=instance['values'], field=instance['filed'])


def save_or_edit_patient(patient, data, type_user):
    fields = get_fields(type_user)
    max_score = 0
    for field in fields:
        score = get_score(
            gender=patient.gender,
            data=data[field.get('name')], birthdate=patient.birthdate, class_name=field.get('_class').__name__,
            type_user=type_user)
        if score > max_score:
            max_score = score
        print(data[field.get('name')])
        save_or_update_instance_form(instance=patient, field=field.get('name'), _class=field.get('_class'),
                                     values={**data[field.get('name')], 'score': score, 'patient': patient})

    if type_user == 'parent':
        patient.score_parent = max_score
    else:
        patient.score_teacher = max_score

    patient.save()
    return patient


us=UserService()
class PatientService(Service):
    def __init__(self, repository=Repository(model=Patient)):
        super().__init__(repository, fields=PATIENT_FIELDS)

    def create(self, data: dict, type_user=None):
        if type_user is None:
            raise ValueError('type_user must not be null')


        patient = self.repository.model()
        patient.name = data.get('name')
        patient.family_name = data.get('family_name')
        patient.is_supervised = False
        patient.birthdate = date.fromisoformat(data.get('birthdate'))
        patient.parent_id = data.get('parent')
        patient.teacher_id = data.get('teacher') if data.get('teacher') is not None else None
        patient.save()
        return save_or_edit_patient(patient=patient, data=data, type_user=type_user)


    def put(self, _id: int, data: dict):
        type_user = data.pop('type_user')
        patient = self.get_by({'id': _id})
        if patient is None:
            raise Patient.DoesNotExist(f'patient does not exists with the following {_id}')
        return save_or_edit_patient(patient=patient, data=data, type_user=type_user)


class SuperviseService(Service):
    def __init__(self, repository=Repository(model=Supervise)):
        super().__init__(repository, fields=SUPERVICE_FIELDS)

    def create(self, data: dict):
        try:
            patient = Patient.objects.get(id=data['patient'])
            doctor = User.objects.get(id=data['doctor'])
        except (Patient.DoesNotExist, User.DoesNotExist):
            return ValueError('Invalid patient or doctor ID')

        data['patient'] = patient
        data['doctor'] = doctor

        supervise = super().create(data)

        if isinstance(supervise, Exception):
            return supervise

        try:
            patient.accepted = False
            patient.is_supervised = True
            patient.save()
        except Exception as exception:
            return exception, patient

        return supervise


class ConsultationService(Service):
    def __init__(self, repository=Repository(model=Consultation)):
        super().__init__(repository, fields=CONSULTATION_FIELDS)


class DiagnosticService(Service):
    def __init__(self, repository=Repository(model=Diagnostic)):
        super().__init__(repository, fields=DIAGNOSTIC_FIELDS)
