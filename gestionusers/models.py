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


class PersonProfileSerializer(ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    profile = PersonProfileSerializer()
    localisation = LocalisationSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'profile', 'login_number', 'type_user', 'telephone', 'localisation']
