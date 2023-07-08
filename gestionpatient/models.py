import django.utils.timezone as timezone
from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, Model, \
    OneToOneField, TextField, FloatField, SET_NULL
from django.db.models import Model
from rest_framework.serializers import ModelSerializer
from gestionusers.serializers import UserSerializer

app_label = 'gestionpatient'
user_model = 'gestionusers.User'


class Patient(Model):
    teacher = ForeignKey(to=user_model, on_delete=SET_NULL, null=True, related_name='patient_teacher')
    parent = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='patient_parent')
    name: TextField = TextField(null=False)
    family_name: TextField = TextField(null=False)
    birthdate: DateField = DateField(null=False)
    gender: TextField = TextField(null=False)
    sick: BooleanField = BooleanField(default=None, null=True)
    score_parent = FloatField(default=0, null=False)
    score_teacher = FloatField(default=0, null=False)
    is_supervised = BooleanField(default=False, null=False)
    is_consulted = BooleanField(default=False, null=False)

    class Meta:
        db_table = 'patients'
        unique_together = (('parent', 'name', 'birthdate'),)


class Supervise(Model):
    patient: OneToOneField = OneToOneField(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=user_model, on_delete=CASCADE, null=False)

    class Meta:
        db_table = 'supervises'


class Consultation(Model):
    doctor: ForeignKey = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='doctor_id')
    patient: OneToOneField = OneToOneField(to='Patient', on_delete=CASCADE, null=False)
    date: DateTimeField = DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'consultations'


class Diagnostic(Model):
    consultation: OneToOneField = OneToOneField(to='Consultation', on_delete=CASCADE)
    patient: ForeignKey = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    diagnostic: TextField = TextField(null=False)

    class Meta:
        db_table = 'diagnostics'


class PatientSerializer(ModelSerializer):
    parent = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'


class SuperviseSerializer(ModelSerializer):
    patient = PatientSerializer()
    doctor = UserSerializer()

    class Meta:
        model = Supervise
        fields = "__all__"


class DiagnosticSerializer(ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'


class ConsultationSerializer(ModelSerializer):
    patient = PatientSerializer()
    doctor = UserSerializer()

    class Meta:
        model = Consultation
        fields = '__all__'
