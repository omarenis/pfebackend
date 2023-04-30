from typing import Union

from django.contrib.auth.models import AnonymousUser
from common.repositories import Repository
from common.services import Service
from .models import Localisation, User, PersonProfile

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
    'type_user': {'type': 'text', 'required': True},
    'profile': {'type': 'one_to_one_field', 'required': True}
}

PROFILE = {
    'family_name': {'type': 'text', 'required': True},
    'school': {'type': 'foreign_key', 'required': False},
    'is_super_doctor': {'type': 'boolean', 'required': False},
    'speciality': {'type': 'text', 'required': True},
    'super_doctor': {'type': 'foreign_key', 'required': False}
}


class UserService(Service):
    def __init__(self, repository=Repository(model=User)):
        super().__init__(repository, fields=USER_FIELDS)

    def create(self, data: dict):
        if (data.get('type_user') != 'admin' or data.get('type_user') != 'school') and data.get('profile').get(
                'family_name') is None:
            raise ValueError('family_name must be not null')

        if data.get('type_suer') == 'teacher' and data.get('profile').get('school') is None:
            raise ValueError('school must be not null')

        if data.get('type_user') == 'doctor':
            if data.get('profile').get('is_super_doctor') is False:
                if data.get('profile').get('speciality') is None:
                    raise ValueError('doctor must have a speciality')
                if data.get('profile').get('super_doctor') is None:
                    raise ValueError('super_doctor must have a super doctor')

        profile = data.pop('profile')

        user = User(**data)
        if profile is not None:
            profile['school_id'] = profile.pop('school')
            profile['super_doctor_id'] = profile.pop('super_doctor')
            user.profile = PersonProfile(**profile)
        user.save()
        return user


class LoginSignUpService(object):
    def __init__(self):
        self.user_service = UserService()

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
        return self.user_service.create(data)


class LocalisationService(Service):
    def __init__(self, repository=Repository(model=Localisation)):
        super().__init__(repository, fields=LOCALISATION_FIELDS)
