from common.repositories import Repository
from common.services import Service, calculate_score
from formparent.models import BehaviorTroubleParent, LearningTroubleParent, SomatisationTroubleParent, \
    HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent

from formteacher.models import BehaviorTroubleTeacher, HyperActivityTroubleTeacher, InattentionTroubleTeacher, \
    FormAbrTeacher
from .matrices import matrix
from .models import Consultation, Diagnostic, Patient, Supervise
from datetime import datetime

URL = "http://localhost:5000/"
APPLICATION_TYPE = "application/json"

PATIENT_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'familyName': {'type': 'text', 'required': True},
    'birthdate': {'type': 'date', 'required': True},
    'parent_id': {'type': 'foreign_key', 'required': False},
    'sick': {'type': 'bool', 'required': False},
    'behaviortroubleparent': {'type': 'BehaviorTroubleParent', 'required': False},
    'learningtroubleparent': {'type': 'LearningTroubleParent', 'required': False},
    'somatisationtroubleparent': {'type': 'SomatisationTroubleParent', 'required': False},
    'hyperactivitytroubleparent': {'type': 'HyperActivityTroubleParent', 'required': False},
    'anxitytroubleparent': {'type': 'AnxityTroubleParent', 'required': False},
    'formabrparent': {'type': 'FormAbrParent', 'required': False},
    'behaviortroubleteacher': {'type': 'behaviorTroubleTeacher', 'required': False},
    'hyperactivitytroubleteacher': {'type': 'hyperActivityTroubleTeacher', 'required': False},
    'inattentiontroubleteacher': {'type': 'inattentionTroubleTeacher', 'required': False},
    'formabrteacher': {'type': 'formAbrTeacher', 'required': False}
}

SUPERVICE_FIELDS = {
    'patient_id': {'type': 'int', 'required': True},
    'doctor_id': {'type': 'int', 'required': True},
    'accepted': {'type': 'bool', 'required': True}
}

CONSULTATION_FIELDS = {
    'doctor_id': {'type': 'int', 'required': True},
    'parent_id': {'type': 'int', 'required': True},
    'date': {'type': 'int', 'required': True},
    'accepted': {'type': 'bool', 'required': True}
}
DIAGNOSTIC_FIELDS = {
    'patient_id': {'type': 'int', 'required': True},
    'diagnostic': {'type': 'str', 'required': True},
    'consultation_id': {'type': 'int', 'required': True}
}


def get_age(birthdate):
    return (datetime.utcnow() - birthdate).total_seconds() // (3600 * 24 * 365)


def get_score(gender, data, birthdate, class_name, type_user):
    return matrix(gender=gender, type_user=type_user,
                  tranche=int(get_age(birthdate=birthdate) // 3))[class_name][calculate_score(data)]


class PatientService(Service):
    def __init__(self, repository=Repository(model=Patient)):
        super().__init__(repository, fields=PATIENT_FIELDS)

    def save_instance_form(self, instance):
        if instance is not None:
            instance.save()

    def create(self, data: dict, type_user=None):
        if type_user is None:
            raise ValueError('type_user must not be null')
        patient = self.repository.model()
        patient.name = data.get('name')
        patient.is_supervised = False
        patient.birthdate = datetime.fromisoformat(data.get('birthdate'))
        behavior_trouble = None
        learning_trouble = None
        somatisation_trouble = None
        hyperactivity_trouble = None
        inattention_trouble = None
        anxity_trouble = None
        form_abr = None
        if type_user == 'parent':
            behavior_trouble = BehaviorTroubleParent(score=get_score(
                gender=data.get('gender'),
                data=data['behaviortroubleparent'], birthdate=patient.birthdate, class_name='BehaviorTroubleParent',
                type_user=type_user),
                **data['behaviortroubleparent'],
            patient=patient)

            learning_trouble = LearningTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['learningtroubleparent'], class_name='LearningTroubleParent', type_user=type_user),
                **data['learningtroubleparent'],
                patient=patient)
            somatisation_trouble = SomatisationTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['somatisationtroubleparent'], class_name='SomatisationTroubleParent', type_user=type_user),
                **data['somatisationtroubleparent'],
                patient=patient)

            hyperactivity_trouble = HyperActivityTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleparent'], class_name='HyperActivityTroubleParent', type_user=type_user),
                **data['hyperactivitytroubleparent'],
                patient=patient)

            anxity_trouble = AnxityTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['anxitytroubleparent'], class_name='AnxityTroubleParent', type_user=type_user),
                **data['anxitytroubleparent'],
                patient=patient)

            form_abr = FormAbrParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['formabrparent'], class_name='FormAbrParent', type_user=type_user),
                **data['formabrparent'],
                patient=patient)

        if type_user == 'teacher':
            behavior_trouble = BehaviorTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['behaviortroubleteacher'], class_name='BehaviorTroubleTeacher', type_user=type_user),
                **data['behaviortroubleteacher'],
                patient=patient)

            hyperactivity_trouble = HyperActivityTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleteacher'], class_name='HyperActivityTroubleTeacher',
                type_user=type_user),
                **data['hyperactivitytroubleteacher'],
                patient=patient)

            inattention_trouble = InattentionTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['inattentiontroubleteacher'], class_name='InattentionTroubleTeacher', type_user=type_user),
                **data['inattentiontroubleteacher'])

            form_abr = FormAbrTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['formabrteacher'], class_name='FormAbrTeacher', type_user=type_user),
                **data['formabrteacher'])
        patient.save()
        self.save_instance_form(behavior_trouble)
        self.save_instance_form(anxity_trouble)
        self.save_instance_form(learning_trouble)
        self.save_instance_form(somatisation_trouble)
        self.save_instance_form(hyperactivity_trouble)
        self.save_instance_form(form_abr)
        self.save_instance_form(inattention_trouble)
        print(behavior_trouble.score)
        return patient


class SuperviseService(Service):
    def __init__(self, repository=Repository(model=Supervise)):
        super().__init__(repository, fields=SUPERVICE_FIELDS)

    def create(self, data: dict):
        supervise = super().create(data)
        if isinstance(supervise, Exception):
            return supervise
        try:
            patient = Patient.objects.get(id=data['patient_id'])
            patient.isSupervised = True
            patient.save()
        except Exception as exception:
            return exception
        return supervise


class ConsultationService(Service):
    def __init__(self, repository=Repository(model=Consultation)):
        super().__init__(repository, fields=CONSULTATION_FIELDS)


class DiagnosticService(Service):
    def __init__(self, repository=Repository(model=Diagnostic)):
        super().__init__(repository, fields=DIAGNOSTIC_FIELDS)
