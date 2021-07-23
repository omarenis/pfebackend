from django.db.models import CASCADE, DateField, EmailField, ForeignKey, Model, SET_DEFAULT, SET_NULL, TextField
from rest_framework.serializers import ModelSerializer


class Patient(Model):
    block = TextField(null=False)
    parent = ForeignKey('gestionusers.Parent', on_delete=CASCADE)
    doctor = ForeignKey('gestionusers.Doctor', on_delete=SET_DEFAULT, default=0)
    parent_full_name: TextField = TextField(null=False)
    parent_email: EmailField = EmailField(null=False)
    parent_phone: TextField = TextField(null=False)
    name: TextField = TextField(null=False, unique=True)
    family_name = TextField(null=False, unique=False)
    birthdate: DateField = DateField()

    class Meta:
        db_table = 'patients'


class Orientation(Model):
    patient: ForeignKey = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to='gestionusers.Doctor', on_delete=SET_NULL, null=True)
    diagnostic: TextField = TextField(null=False)

    class Meta:
        db_table = 'orientations'


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class OrientationSerializer(ModelSerializer):
    class Meta:
        model = Orientation
        fields = '__all__'
