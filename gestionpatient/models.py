from django.db.models import CASCADE, DateField, ForeignKey, Model, SET_NULL, TextField
from datetime import date
from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, ManyToManyField, Model, \
    OneToOneField, TextField, FloatField, __all__
from rest_framework.serializers import ModelSerializer
from common.models import create_model_serializer
import django.utils.timezone as timezone
from gestionusers.models import PersonSerializer

app_label = 'gestionpatient'
doctor_model = 'gestionusers.Doctor'


class Patient(Model):
    parent = ForeignKey(to='gestionusers.Parent', on_delete=CASCADE, null=True)
    name: TextField = TextField(null=False)
    school: TextField = TextField(null=False)
    birthdate: DateField = DateField(null=False)
    gender: TextField = TextField(null=False, default='ذكر')
    sick: BooleanField = BooleanField(default=None, null=True)
    score_parent = FloatField(default=0, null=False)
    score_teacher = FloatField(default=0, null=False)
    is_supervised = BooleanField(default=False, null=False)

    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def tr_age(self):
        return self.age() // 3

    class Meta:
        db_table = 'patients'
        unique_together = (('parent', 'name', 'school', 'birthdate'),)


class Supervise(Model):
    patient: OneToOneField = OneToOneField(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=doctor_model, on_delete=CASCADE, null=False)
    accepted: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'supervises'


class Consultation(Model):
    doctor: ForeignKey = ForeignKey(to=doctor_model, on_delete=CASCADE, null=False)
    parent: ForeignKey = ForeignKey(to='gestionusers.Parent', on_delete=CASCADE, null=False)
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


# SuperviseSerializer = create_model_serializer(model=Supervise, app_label=app_label, name='SuperviseSerializer')
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
