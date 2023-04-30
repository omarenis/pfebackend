from typing import Union

from django.contrib.auth.models import AnonymousUser
from common.repositories import Repository
from common.services import Service
from .models import Doctor, Localisation, Teacher, User, Parent


URL = "http://localhost:5000/"


LOCALISATION_FIELDS = {
    'governorate': {'type': 'text', 'required': True},
    'delegation': {'type': 'text', 'required': True},
    'zip_code': {'type': 'text', 'required': True}
}

USER_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'login_number': {'type': 'text', 'required': True},
    'email': {'type': 'email', 'required': False},
    'telephone': {'type': 'email', 'required': True},
    'password': {'type': 'password', 'required': True},
    'type_user': {'type': 'text', 'required': True}
}

PERSON_FIELDS = {
    **USER_FIELDS,
    'localisation_id': {'type': 'integer', 'required': False},
    'family_name': {'type': 'text', 'required': True}
}

DOCTOR_FIELDS = {
    **PERSON_FIELDS,
    'speciality': {'type': 'text', 'required': False},
    'is_super': {'type': 'bool', 'required': False},
    'super_doctor': {'type': 'foreign_key', 'required': False},
}


class UserService(Service):
    def __init__(self, repository=Repository(model=User)):
        super().__init__(repository, fields=USER_FIELDS)

    def retrieve(self, _id: int):
        user = super().retrieve(_id)
        if user.type_user == 'doctor':
            return DoctorService().retrieve(_id=_id)
        return user


class LoginSignUpService(object):
    def __init__(self):
        self.user_service = UserService()
        self.person_service = PersonService()

    def login(self, login_number: str, password: str):
        user = self.user_service.get_by({'login_number': login_number})
        if user is not None and user.is_active:
            if user.check_password(password):
                return user
            elif not user.is_active:
                raise PermissionError('الحساب غير مفعّل')
            else:
                raise ValueError('كلمة السر غير صحيحة')
        else:
            raise User.DoesNotExist('الحساب غير موجود')

    def signup(self, data: dict):
        localisation_id = data.get('localisation_id')
        if data.get('localisation_id') is None:
            localisation_service = LocalisationService()
            localisation = localisation_service.filter_by(data.get('localisation')).first()
            if localisation is None:
                localisation = localisation_service.create(data=data.get('localisation'))
            if isinstance(localisation, Exception):
                return localisation
            localisation_id = localisation.id
        data['is_active'] = True
        data['localisation_id'] = localisation_id
        data['type_user'] = 'parent'
        return self.person_service.create(data)


class PersonService(Service):
    def __init__(self, repository=Repository(model=Union[Parent, Teacher])):
        super().__init__(repository, fields=PERSON_FIELDS)

    def reset_password(self, _id: int, password):
        user = self.repository.retrieve(_id)
        if user is None:
            return Exception("user not found")
        else:
            user.set_password(password)
        return user

    def filter_by(self, data: dict):
        if data.get('type_user') == 'teacher':
            self.repository = Repository(model=Teacher)
        return self.repository.filter_by(data=data)


class LocalisationService(Service):
    def __init__(self, repository=Repository(model=Localisation)):
        super().__init__(repository, fields=LOCALISATION_FIELDS)


class DoctorService(Service):
    def __init__(self, repository=Repository(model=Doctor)):
        super().__init__(repository, fields=DOCTOR_FIELDS)
