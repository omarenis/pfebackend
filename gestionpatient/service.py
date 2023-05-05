from common.repositories import Repository
from common.services import Service, calculate_score
from formparent.models import BehaviorTroubleParent, LearningTroubleParent, SomatisationTroubleParent, \
    HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent

from formteacher.models import BehaviorTroubleTeacher, HyperActivityTroubleTeacher, InattentionTroubleTeacher, \
    FormAbrTeacher, FormTeacher
from gestionusers.models import PersonProfile,User
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
    'patient': {'type': 'one_to_one', 'required': True},
    'doctor': {'type': 'foreign_key', 'required': True},
    'accepted': {'type': 'bool', 'required': True}
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
        form = None
        if type_user == 'parent':
            behavior_trouble = BehaviorTroubleParent(score=get_score(
                gender=data.get('gender'),
                data=data['behaviortroubleparent'], birthdate=patient.birthdate, class_name='BehaviorTroubleParent',
                type_user=type_user),
                **data['behaviortroubleparent'],
                patient=patient)
            print(User.objects.all())
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
            patient.score_parent=max(form_abr.score,anxity_trouble.score,hyperactivity_trouble.score,somatisation_trouble.score,learning_trouble.score,behavior_trouble.score)
        if type_user == 'teacher':
            form = FormTeacher()
            form.patient = patient
            form.teacher =PersonProfile.objects.first()
            print(User.objects.all())
            
            behavior_trouble = BehaviorTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['behaviortroubleteacher'], class_name='BehaviorTroubleTeacher', type_user=type_user),
                **data['behaviortroubleteacher'],
                form=form)

            hyperactivity_trouble = HyperActivityTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleteacher'], class_name='HyperActivityTroubleTeacher',
                type_user=type_user),
                **data['hyperactivitytroubleteacher'],
                form=form)
            print(hyperactivity_trouble.score)
            inattention_trouble = InattentionTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['inattentiontroubleteacher'], class_name='InattentionTroubleTeacher', type_user=type_user),
                **data['inattentiontroubleteacher'],
                form=form)

            form_abr = FormAbrTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['formabrteacher'], class_name='FormAbrTeacher', type_user=type_user),
                **data['formabrteacher'],
                form=form)
            patient.score_teacher=max(behavior_trouble.score,hyperactivity_trouble.score,inattention_trouble.score,form_abr.score)
        
        patient.save()
        if form is not None:
            form.save()
        self.save_instance_form(behavior_trouble)
        self.save_instance_form(anxity_trouble)
        self.save_instance_form(learning_trouble)
        self.save_instance_form(somatisation_trouble)
        self.save_instance_form(hyperactivity_trouble)
        self.save_instance_form(form_abr)
        self.save_instance_form(inattention_trouble)
        return patient


class SuperviseService(Service):
    def __init__(self, repository=Repository(model=Supervise)):
        super().__init__(repository, fields=SUPERVICE_FIELDS)

    def create(self, data: dict):
        try:
            patient = Patient.objects.get(id=data['patient'])
            doctor = PersonProfile.objects.get(id=data['doctor'])
        except (Patient.DoesNotExist, PersonProfile.DoesNotExist):
            return ValueError('Invalid patient or doctor ID')

        data['patient'] = patient
        data['doctor'] = doctor

        supervise = super().create(data)

        if isinstance(supervise, Exception):
            return supervise

        try:
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
