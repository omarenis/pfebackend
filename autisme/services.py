from common.models import text_field
from common.repositories import Repository
from common.services import Service, autismelvl1

from gestionusers.models import User
from gestionusers.services import UserService
from .models import Consultation, Autiste, Supervise, Level1
from .repositories import Level1repository

URL = "http://localhost:5000/"
APPLICATION_TYPE = "application/json"
from datetime import date

AUTISTE_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'family_name': {'type': 'text', 'required': True},
    'birthdate': {'type': 'date', 'required': True},
    'gender': {'type': 'text', 'required': True},
    'parent': {'type': 'foreign_key', 'required': True},
    'score_mother': {'type': 'number', 'required': False},
    'score_father': {'type': 'number', 'required': False},
    "level1": {'type': 'form', 'required': False}
}

level1_fields = {
    "looks_at_pointed_item": text_field,
    "possibly_deaf": text_field,
    "pretending_playing": text_field,
    "climbing_things": text_field,
    "unusual_moves_next_to_eyes": text_field,
    "point_to_get_assistance": text_field,
    "point_to_show_smth": text_field,
    "cares_abt_other_children": text_field,
    "bring_smth_to_show": text_field,
    "response_to_his_name": text_field,
    "smiles_back": text_field,
    "annoyed_by_daily_noise": text_field,
    "walks": text_field,
    "makes_eye_contact": text_field,
    "imitate_parent_action": text_field,
    "turn_head_like_parent": text_field,
    "make_parent_watch": text_field,
    "understand_assignments": text_field,
    "check_parent_reaction": text_field,
    "loves_dynamic_activities": text_field,
    "type_parent": {'type': 'text', 'required': True},
    "parent": {"type": "foreign_key", "required": True},
    "patient": {"type": "foreign_key", "required": True}
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


us = UserService()


class AutisteService(Service):
    def __init__(self, repository=Repository(model=Autiste)):
        super().__init__(repository, fields=AUTISTE_FIELDS)

    def create(self, data: dict):

        aut = self.repository.model()
        aut.name = data.get('name')
        aut.family_name = data.get('family_name')
        aut.is_supervised = False
        aut.gender = data.get('gender')
        aut.birthdate = date.fromisoformat(data.get('birthdate'))
        aut.parent_id = data.get('parent').id
        leveel1 = Level1()
        leveel1.parent = data['parent']
        leveel1.patient = aut
        if data.get('level1').get('type_parent') == 'mother':
            aut.score_mother, leveel1 = autismelvl1(data['level1'], leveel1)
        else:
            aut.score_father, leveel1 = autismelvl1(data['level1'], leveel1)
        if aut.score_father > 8 or aut.score_mother > 8:
            aut.sick = True
        aut.save()
        leveel1.save()
        return aut


class Level1service(Service):
    def __init__(self, repository=Level1repository()):
        super().__init__(repository, fields=level1_fields)


class SuperviseService(Service):
    def __init__(self, repository=Repository(model=Supervise)):
        super().__init__(repository, fields=SUPERVICE_FIELDS)

    def create(self, data: dict):
        try:
            patient = Autiste.objects.get(id=data['patient'])
            doctor = User.objects.get(id=data['doctor'])
        except (Autiste.DoesNotExist, User.DoesNotExist):
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
        except (Autiste.DoesNotExist, User.DoesNotExist):
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
