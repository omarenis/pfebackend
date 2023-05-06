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
    'family_name': {'type': 'text', 'required': True},
    'birthdate': {'type': 'date', 'required': True},
    'gender': {'type': 'text', 'required': True},
    
    'parent_id': {'type': 'foreign_key', 'required': False},
    'teacher_id': {'type': 'foreign_key', 'required': False},
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

#in this case we r creating all the classes since the creation of the patient,and we'll specify which one to edit when we fill the 2nd form
        behavior_trouble_parent = None
        learning_trouble_parent = None
        somatisation_trouble_parent = None
        hyperactivity_trouble_parent = None
        anxity_trouble_parent = None
        form_abr_parent = None
        

        behavior_trouble_teacher=None
        hyperactivity_trouble_teacher = None
        inattention_trouble_teacher = None
        form_abr_teacher = None

        if type_user == 'parent':
            behavior_trouble_parent = BehaviorTroubleParent(score=get_score(
                gender=data.get('gender'),
                data=data['behaviortroubleparent'], birthdate=patient.birthdate, class_name='BehaviorTroubleParent',
                type_user=type_user),
                **data['behaviortroubleparent'],
                )
            
            learning_trouble_parent = LearningTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['learningtroubleparent'], class_name='LearningTroubleParent', type_user=type_user),
                **data['learningtroubleparent'],
                )
            somatisation_trouble_parent = SomatisationTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['somatisationtroubleparent'], class_name='SomatisationTroubleParent', type_user=type_user),
                **data['somatisationtroubleparent'],
                )

            hyperactivity_trouble_parent = HyperActivityTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleparent'], class_name='HyperActivityTroubleParent', type_user=type_user),
                **data['hyperactivitytroubleparent'],
                )

            anxity_trouble_parent = AnxityTroubleParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['anxitytroubleparent'], class_name='AnxityTroubleParent', type_user=type_user),
                **data['anxitytroubleparent'],
                )

            form_abr_parent = FormAbrParent(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['formabrparent'], class_name='FormAbrParent', type_user=type_user),
                **data['formabrparent'],
                patient=patient)
            patient.score_parent=max(form_abr_parent.score,anxity_trouble_parent.score,hyperactivity_trouble_parent.score,somatisation_trouble_parent.score,learning_trouble_parent.score,behavior_trouble_parent.score)
            
        
        if type_user == 'teacher':
            behavior_trouble_teacher = BehaviorTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['behaviortroubleteacher'], class_name='BehaviorTroubleTeacher', type_user=type_user),
                **data['behaviortroubleteacher'],patient=patient
                )

            hyperactivity_trouble_teacher = HyperActivityTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleteacher'], class_name='HyperActivityTroubleTeacher',
                type_user=type_user),
                **data['hyperactivitytroubleteacher'],patient=patient
                )
            
            inattention_trouble_teacher = InattentionTroubleTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['inattentiontroubleteacher'], class_name='InattentionTroubleTeacher', type_user=type_user),
                **data['inattentiontroubleteacher'],patient=patient
            )
            form_abr_teacher = FormAbrTeacher(score=get_score(
                gender=data.get('gender'),
                birthdate=patient.birthdate,
                data=data['formabrteacher'], class_name='FormAbrTeacher', type_user=type_user),
                **data['formabrteacher'],patient=patient
                )
            patient.score_teacher=max(behavior_trouble_teacher.score,hyperactivity_trouble_teacher.score,inattention_trouble_teacher.score,form_abr_teacher.score)
            
        patient.save()
        
        self.save_instance_form(behavior_trouble_parent)
        self.save_instance_form(anxity_trouble_parent)
        self.save_instance_form(learning_trouble_parent)
        self.save_instance_form(somatisation_trouble_parent)
        self.save_instance_form(hyperactivity_trouble_parent)
        self.save_instance_form(form_abr_parent)


        self.save_instance_form(behavior_trouble_teacher)
        self.save_instance_form(hyperactivity_trouble_teacher)
        self.save_instance_form(inattention_trouble_teacher)
        self.save_instance_form(form_abr_teacher)
        print(form_abr_teacher.score)
        return patient





    def edit(self,data:dict,patient: Patient,type_user=None):
        if type_user is None:
            raise ValueError('type_user must not be null')

           
        if type_user == 'parent':    
            behavior_trouble_parent = BehaviorTroubleParent(score=get_score(
                gender=patient.gender,
                data=data['behaviortroubleparent'], birthdate=patient.birthdate, class_name='BehaviorTroubleParent',
                type_user=type_user),
                **data['behaviortroubleparent'],patient=patient
                )
            
            learning_trouble_parent = LearningTroubleParent(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['learningtroubleparent'], class_name='LearningTroubleParent', type_user=type_user),
                **data['learningtroubleparent'],patient=patient
                )
            somatisation_trouble_parent = SomatisationTroubleParent(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['somatisationtroubleparent'], class_name='SomatisationTroubleParent', type_user=type_user),
                **data['somatisationtroubleparent'],patient=patient
                )

            hyperactivity_trouble_parent = HyperActivityTroubleParent(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleparent'], class_name='HyperActivityTroubleParent', type_user=type_user),
                **data['hyperactivitytroubleparent'],patient=patient
                )

            anxity_trouble_parent = AnxityTroubleParent(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['anxitytroubleparent'], class_name='AnxityTroubleParent', type_user=type_user),
                **data['anxitytroubleparent'],patient=patient
                )

            form_abr_parent = FormAbrParent(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['formabrparent'], class_name='FormAbrParent', type_user=type_user),
                **data['formabrparent'],
                patient=patient)
            patient.score_parent=max(form_abr_parent.score,anxity_trouble_parent.score,hyperactivity_trouble_parent.score,somatisation_trouble_parent.score,learning_trouble_parent.score,behavior_trouble_parent.score)
            self.save_instance_form(behavior_trouble_parent)
            self.save_instance_form(anxity_trouble_parent)
            self.save_instance_form(learning_trouble_parent)
            self.save_instance_form(somatisation_trouble_parent)
            self.save_instance_form(hyperactivity_trouble_parent)
            self.save_instance_form(form_abr_parent)


        if type_user == 'teacher':
            behavior_trouble_teacher = BehaviorTroubleTeacher(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['behaviortroubleteacher'], class_name='BehaviorTroubleTeacher', type_user=type_user),
                **data['behaviortroubleteacher'],patient=patient
                )

            hyperactivity_trouble_teacher = HyperActivityTroubleTeacher(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['hyperactivitytroubleteacher'], class_name='HyperActivityTroubleTeacher',
                type_user=type_user),
                **data['hyperactivitytroubleteacher'],patient=patient
                )
            
            inattention_trouble_teacher = InattentionTroubleTeacher(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['inattentiontroubleteacher'], class_name='InattentionTroubleTeacher', type_user=type_user),
                **data['inattentiontroubleteacher'],patient=patient
            )
            form_abr_teacher = FormAbrTeacher(score=get_score(
                gender=patient.gender,
                birthdate=patient.birthdate,
                data=data['formabrteacher'], class_name='FormAbrTeacher', type_user=type_user),
                **data['formabrteacher'],patient=patient
                )
            
            patient.score_teacher=max(behavior_trouble_teacher.score,hyperactivity_trouble_teacher.score,inattention_trouble_teacher.score,form_abr_teacher.score)
            

        self.save_instance_form(behavior_trouble_parent)
        self.save_instance_form(anxity_trouble_parent)
        self.save_instance_form(learning_trouble_parent)
        self.save_instance_form(somatisation_trouble_parent)
        self.save_instance_form(hyperactivity_trouble_parent)           
        self.save_instance_form(form_abr_parent)    


        self.save_instance_form(behavior_trouble_teacher)
        self.save_instance_form(hyperactivity_trouble_teacher)
        self.save_instance_form(inattention_trouble_teacher)
        self.save_instance_form(form_abr_teacher)


        patient.save()
        

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
            patient.accepted=False
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
