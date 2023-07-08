from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import CASCADE, CharField, EmailField, ForeignKey, Model, OneToOneField, SET_NULL, TextField, \
    BooleanField, BigIntegerField
from rest_framework.serializers import ModelSerializer, Serializer

app_label = 'gestionusers'


class Governorate(Model):
    governorate: TextField = TextField(null=False)

    class Meta:
        db_table = 'governorate'


class Delegation(Model):
    delegation: TextField = TextField(null=False)
    governorate = ForeignKey(to=Governorate, on_delete=CASCADE, null=False)

    class Meta:
        db_table = 'delegation'


class Localisation(Model):
    country = CharField(max_length=255)
    state = CharField(max_length=100, verbose_name='state')
    delegation = CharField(max_length=100, verbose_name='delegation')
    zip_code = CharField(max_length=4, verbose_name='zip_code')

    class Meta:
        unique_together = (('country', 'state', 'delegation', 'zip_code'),)


class User(AbstractUser):
    name = TextField(null=False)
    login_number = CharField(null=False, unique=True, max_length=9, db_column='login_number')
    telephone = TextField(null=False)
    telephone2 = TextField(null=True, default=None)
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
