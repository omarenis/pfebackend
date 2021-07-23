from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import CharField, EmailField, Model, TextField
from rest_framework.serializers import ModelSerializer


class Localisation(Model):
    governorate: TextField = TextField(null=False)
    delegation: TextField = TextField(null=False)
    zip_code: TextField = TextField(null=False, max_length=4)

    class Meta:
        db_table = 'localisations'
        unique_together = ('governorate', 'delegation', 'zip_code')


class UserManager(BaseUserManager):
    def create_user(self, name, family_name, cin, telephone, email, password, type_user):
        data = {'name': name, 'family_name': family_name, 'cin': cin, 'telephone': telephone,
                'email': self.normalize_email(email), 'accountId': None}

        try:
            if type_user == 'parent':
                user = Parent(**data)
            elif type_user == 'doctor':
                user = Doctor(**data)
            else:
                raise AttributeError('user must be parent or doctor')
            user.username = name + ' ' + family_name
            user.set_password(password)
            user.save()
            return user
        except Exception as exception:
            return exception


class Person(AbstractUser):
    objects: UserManager = UserManager()
    name: TextField = TextField(null=False)
    family_name: TextField = TextField(null=False)
    cin: CharField = CharField(max_length=255, null=False, unique=True)
    email: EmailField = EmailField(null=False, unique=True)
    telephone: CharField = CharField(max_length=255, null=False, unique=True)
    password: TextField = TextField(null=False)
    accountId: TextField = TextField(null=True, db_column='account_id')

    class Meta:
        db_table = 'persons'


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        excludes = ['password', 'accountId']


class Parent(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Doctor(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LocalisationSerializer(ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'
        excludes = ['person_set']
