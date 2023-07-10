from rest_framework.serializers import Serializer, CharField, BooleanField, RelatedField, ModelSerializer
from gestionusers.models import User, Governorate, PersonProfile


class LocalisationSerializer(Serializer):
    country = CharField(max_length=255)
    state = CharField(max_length=100)
    delegation = CharField(max_length=100)
    zip_code = CharField(max_length=4)


class PersonProfileSerializer(ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = '__all__'


class UserSerializer(Serializer):
    name = CharField()
    login_number = CharField()
    telephone = CharField()
    telephone2 = CharField()
    address = CharField()
    type_user = CharField()
    localisation = LocalisationSerializer()
    profile = PersonProfileSerializer()


class GovernorateSerializer(Serializer):
    governorate = CharField()


class DelegationSerializer(Serializer):
    delegation: CharField = CharField()
    governorate = RelatedField(queryset=Governorate.objects.using('default').all())
