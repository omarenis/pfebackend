import django.utils.timezone as timezone
from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, Model, \
    OneToOneField, TextField, FloatField
from django.db.models import Model
from rest_framework.serializers import ModelSerializer

app_label = 'gestionpatient'
person_profile_model = 'gestionusers.PersonProfile'


class Patient(Model):
    teacher = ForeignKey(to=person_profile_model, on_delete=CASCADE, null=True, related_name='patient_teacher')
    parent = ForeignKey(to=person_profile_model, on_delete=CASCADE, null=True, related_name='patient_parent')
    name: TextField = TextField(null=False)
    birthdate: DateField = DateField(null=False)
    gender: TextField = TextField(null=False, default='M')
    sick: BooleanField = BooleanField(default=None, null=True)
    score_parent = FloatField(default=0, null=False)
    score_teacher = FloatField(default=0, null=False)
    is_supervised = BooleanField(default=False, null=False)

    class Meta:
        db_table = 'patients'
        unique_together = (('parent', 'name', 'birthdate'),)


class Supervise(Model):
    patient: OneToOneField = OneToOneField(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=person_profile_model, on_delete=CASCADE, null=False)
    accepted: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'supervises'


class Consultation(Model):
    doctor: ForeignKey = ForeignKey(to=person_profile_model, on_delete=CASCADE, null=False, related_name='doctor_id')
    parent: ForeignKey = ForeignKey(to=person_profile_model, on_delete=CASCADE, null=False, related_name='parent_id')
    date: DateTimeField = DateTimeField(null=False, default=timezone.now)
    accepted: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'consultations'


class Diagnostic(Model):
    consultation: OneToOneField = OneToOneField(to='Consultation', on_delete=CASCADE)
    patient: ForeignKey = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    diagnostic: TextField = TextField(null=False)

    class Meta:
        db_table = 'diagnostics'


class SuperviseSerializer(ModelSerializer):
    class Meta:
        model = Supervise
        fields = "__all__"


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DiagnosticSerializer(ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'


class ConsultationSerializer(ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'
