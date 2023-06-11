from common.repositories import Repository
from common.services import Service, calculate_score,autismelvl1,autismelvl2

from formTSA.models import level1,level2
from gestionusers.models import PersonProfile, User
from gestionusers.services import UserService

from .models import Consultation, Autiste, Supervise
from datetime import date

URL = "http://localhost:5000/"
APPLICATION_TYPE = "application/json"
from datetime import date


mentalage=[6,6,6,6,6,6,12,12,13,14,15,15,16,16,17,17,18,19,20,21,22,23,24,24,25,25,26,27,27,28,28,29,30,31,31,32,33,34,34,35,36,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,58,60,62,63,65,69,73,78,83]


AUTISTE_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'family_name': {'type': 'text', 'required': True},
    'birthdate': {'type': 'date', 'required': True},
    'gender': {'type': 'text', 'required': True},
    'parent': {'type': 'foreign_key', 'required': True},
    
    'level1': {'type': 'level1', 'required': True},
    'level2': {'type': 'level2', 'required': True},


}

SUPERVICE_FIELDS = {
    'patient': {'type': 'one_to_one', 'required': True},
    'doctor': {'type': 'foreign_key', 'required': True}
    
}

CONSULTATION_FIELDS = {
    'doctor': {'type': 'foreign_key', 'required': True},
    'patient': {'type': 'one_to_one', 'required': True},
    'date': {'type': 'int', 'required': True},
}




def get_age(birthdate):
    
    return (date.today() - birthdate).total_seconds() // (3600 * 24 * 365)


def score2(data):
    return mentalage[autismelvl2(data)]


us=UserService()
class AutisteService(Service):
    def __init__(self, repository=Repository(model=Autiste)):
        super().__init__(repository, fields=AUTISTE_FIELDS)

    def create(self, data: dict):
        
        Aut = self.repository.model()
        Aut.name = data.get('name')
        Aut.family_name = data.get('family_name')
        Aut.is_supervised = False
        Aut.gender=data.get('gender')
        Aut.birthdate = date.fromisoformat(data.get('birthdate'))
        Aut.parent_id = data.get('parent')
        if data.get('type_parent')=='mother':
            Aut.score_mother=autismelvl1(data['level1'])
        else:
            Aut.score_teacher=autismelvl1(data['level1'])
        
        Aut.save()
        return Aut
        



class SuperviseService(Service):
    def __init__(self, repository=Repository(model=Supervise)):
        super().__init__(repository, fields=SUPERVICE_FIELDS)

    def create(self, data: dict):
        try:
            patient = Autiste.objects.get(id=data['patient'])
            doctor = User.objects.get(id=data['doctor'])
        except (patient.DoesNotExist, User.DoesNotExist):
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
    def create(self, data: dict):
        try:
            patient = Autiste.objects.get(id=data['patient'])
            doctor = User.objects.get(id=data['doctor'])
        except (patient.DoesNotExist, User.DoesNotExist):
            return ValueError('Invalid patient or doctor ID')

        data['patient'] = patient
        data['doctor'] = doctor

        consultation = super().create(data)

        if isinstance(consultation, Exception):
            return consultation
        try:
            
            patient.is_consulted = True
            patient.save()
        except Exception as exception:
            return exception, patient

        

        return consultation


