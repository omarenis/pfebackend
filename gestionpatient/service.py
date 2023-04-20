from common.repositories import Repository
from common.services import Service, calculate_score
from formparent.models import BehaviorTroubleParent, LearningTroubleParent, SomatisationTroubleParent, \
    HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent
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


def get_score(data, class_name, type_user):
    return  matrix(gender=data.get('gender'), type_user=type_user, tranche=get_age(data.get('birthdate')) // 3)[class_name][calculate_score(data, fields=list(data.keys()))]



class PatientService(Service):
    def __init__(self, repository=Repository(model=Patient)):
        super().__init__(repository, fields=PATIENT_FIELDS)

    def create(self, data: dict, type_user=None):
        if type_user is None:
            raise Exception('type_user must not be   null')
        patient = self.repository.model()
        patient.name = data.get('name')
        patient.is_supervised = False
        patient.birthdate = data.get('birthdate')
        if type_user == 'parent':
            data['behaviortroubleparent'] = BehaviorTroubleParent(score=get_score(
                data=data['behaviortroubleparent'], class_name='BehaviorTroubleParent', type_user=type_user),
                **data['behaviortroubleparent'])

            data['learningtroubleparent'] = LearningTroubleParent(**data.pop('learningtroubleparent'))
            data['somatisationtroubleparent'] = SomatisationTroubleParent(**data.pop('somatisationtroubleparent'))
            data['hyperactivitytroubleparent'] = HyperActivityTroubleParent(**data.pop('hyperactivitytytroubleparent'))
            data['anxitytroubleparent'] = AnxityTroubleParent(**data.pop('anxitytroubleparent'))
            data['formabrparent'] = FormAbrParent(score=get_score(data=data['formabrparent']), **data.pop('formabrparent'))


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
