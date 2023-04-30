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
        if type_user == 'admin':
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
            'login_number': login_number,
            'telephone': telephone,
            'type_user': type_user,
            'address': address,
            'is_active': is_active,
            'is_superuser': False,
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


class Localisation(Model):
    state = CharField(max_length=100, verbose_name='state')
    delegation = CharField(max_length=100, verbose_name='delegation')
    zip_code = CharField(max_length=4, verbose_name='zip_code')

    class Meta:
        unique_together = (('state', 'delegation', 'zip_code'),)


class User(AbstractUser):
    name = TextField(null=False)
    login_number = CharField(null=False, unique=True, max_length=9, db_column='login_number')
    telephone = TextField(null=False)
    address = TextField(null=True, default=None)
    type_user = TextField(null=False, db_column='type_user')
    localisation = ForeignKey(null=True, to='Localisation', on_delete=SET_NULL)
    profile = OneToOneField(to='PersonProfile', on_delete=CASCADE, null=True)

    class Meta:
        db_table = 'users'


class PersonProfile(Model):
    family_name = TextField(null=False)
    school = ForeignKey(to='User', on_delete=CASCADE, null=True)
    is_super_doctor = BooleanField(null=True, default=False)
    speciality = TextField(null=True)
    super_doctor = ForeignKey(to='PersonProfile', on_delete=CASCADE, null=True)

    class Meta:
        db_table = 'person_profiles'


class LocalisationSerializer(ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PersonProfileSerializer(ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = '__all__'
