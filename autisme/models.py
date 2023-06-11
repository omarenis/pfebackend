import django.utils.timezone as timezone
from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, Model, \
    OneToOneField, TextField, FloatField, SET_NULL
from django.db.models import Model
from rest_framework.serializers import ModelSerializer

from gestionusers.models import UserSerializer


user_model='gestionusers.User'


class Autiste(Model):
    parent = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='autiste_parent')
    name: TextField = TextField(null=False)
    family_name:TextField = TextField(null=False)
    birthdate: DateField = DateField(null=False)
    gender: TextField = TextField(null=False)
    score_father = FloatField(default=0, null=False)
    score_mother = FloatField(default=0, null=False)
    is_supervised = BooleanField(default=False, null=False)
    sick=BooleanField(default=False, null=False)
    is_consulted = BooleanField(default=False, null=False)
    mentalage=FloatField(null=True)
    class Meta:
        db_table = 'TSA_patients'
        unique_together = (('parent', 'name', 'birthdate'),)


class Supervise(Model):
    subject: OneToOneField = OneToOneField(to='Autiste', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='id_doctor')

    class Meta:
        db_table = 'supervises_autisme'


class Consultation(Model):
    doctor: ForeignKey = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='doctor_idd')
    subject: OneToOneField = OneToOneField(to='Autiste', on_delete=CASCADE, null=False, related_name='autiste_id')
    date: DateTimeField = DateTimeField(null=False, default=timezone.now)
    

    class Meta:
        db_table = 'consultations_autisme'



class AutisteSerializer(ModelSerializer):
    parent = UserSerializer()
    
   
    class Meta:
        model = Autiste
        fields = '__all__'


class SuperviseSerializer(ModelSerializer):
    patient=AutisteSerializer()
    doctor=UserSerializer()
    class Meta:
        model = Supervise
        fields = "__all__"




class ConsultationSerializer(ModelSerializer):
    patient=AutisteSerializer()
    doctor=UserSerializer()
    class Meta:
        model = Consultation
        fields = '__all__'
