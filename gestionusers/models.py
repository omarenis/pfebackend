import string
from random import choices
from typing import Union

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import CASCADE, CharField, EmailField, ForeignKey, Model, OneToOneField, SET_NULL, TextField, \
    BooleanField, BigIntegerField
from rest_framework.serializers import ModelSerializer, Serializer

app_label = 'gestionusers'


# create the user manager and the person manager
class UserManager(BaseUserManager):
    def create(self, name: str, login_number: str, telephone: str, password: str, type_user: str, localisation_id=None,
               email=None):
        data = {
            'name': name,
            'loginNumber': login_number,
            'telephone': telephone,
            'type_user': type_user,
            'localisation_id': localisation_id,
            'email': self.normalize_email(email) if email is not None else None,
            'username': login_number
        }
        if type_user == 'school':
            user = School(**data)
        else:
            data['is_active'] = True
            data['is_superuser'] = True
            data['is_staff'] = True
            user = self.model(**data)
        user.set_password(password)
        user.save()
        return user


class PersonManager(BaseUserManager):
    def create(self, name: str, login_number: str, telephone: str, type_user: str, family_name: str,
               localisation_id, address=None, email=None, is_active=False, password=None):
        data = {
            'name': name,
            'family_name': family_name,
            'loginNumber': login_number,
            'telephone': telephone,
            'type_user': type_user,
            'address': address,
            'is_active': is_active,
            'email': self.normalize_email(email) if email is not None else email,
            'localisation_id': localisation_id,
            'username': login_number
        }
        user = self.model(**data)
        random_str = ''.join(choices(string.ascii_letters + string.digits, k=1258)) if not is_active else \
            password
        user.set_password(random_str)
        user.save()
        return user


class DoctorManager(BaseUserManager):
    def create(self, name: str, login_number: str, telephone: str, family_name: str,
               email, address, localisation_id, is_super, password, speciality,
               super_doctor_id=None):
        data = {
            'name': name,
            'family_name': family_name,
            'loginNumber': login_number,
            'telephone': telephone,
            'type_user': 'doctor',
            'address': address,
            'is_active': True,
            'email': self.normalize_email(email),
            'localisation_id': localisation_id,
            'username': login_number,
            'is_super': is_super,
            'speciality': speciality,
            'super_doctor_id': None
        }
        doctor = self.model(**data)
        doctor.set_password(password)
        doctor.save()
        return doctor


class Localisation(Model):
    state = CharField(max_length=100, verbose_name='state')
    delegation = CharField(max_length=100, verbose_name='delegation')
    zip_code = CharField(max_length=4, verbose_name='zip_code')

    class Meta:
        unique_together = ('state', 'delegation', 'zip_code')


class User(AbstractUser):
    name = TextField(null=False)
    login_number = CharField(null=False, unique=True, max_length=9, db_column='login_number')
    telephone = TextField(null=False)
    address = TextField(null=True, default=None)
    type_user = TextField(null=False, db_column='type_user')
    localisation = ForeignKey(null=True, to='Localisation', on_delete=SET_NULL)
    objects = PersonManager()


class Parent(User):
    family_name = TextField(null=False)
    objects = PersonManager()

    class Meta:
        db_table = 'parents'


class Teacher(User):
    family_name = TextField(null=False)
    parent_school = ForeignKey(to='School', on_delete=CASCADE, null=False)
    objects = PersonManager()

    class Meta:
        db_table = 'teachers'


class School(User):
    class Meta:
        db_table = 'schools'


class Doctor(User):
    is_super = BooleanField(null=False, default=False)
    speciality = TextField(null=False)
    super_doctor = ForeignKey(to='Doctor', on_delete=SET_NULL, null=True)
    objects = DoctorManager()

    class Meta:
        db_table = 'doctors'


class LocalisationSerializer(ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Union[Teacher, Parent]
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
