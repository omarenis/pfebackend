import django.utils.timezone as timezone
from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, Model, \
    OneToOneField, TextField, FloatField, SET_NULL, CharField
from django.db.models import Model
from rest_framework.serializers import ModelSerializer

from gestionusers.serializers import UserSerializer

user_model = 'gestionusers.User'


class Autiste(Model):
    parent = ForeignKey(to=user_model, on_delete=CASCADE, null=False, related_name='autiste_parent')
    name: TextField = TextField(null=False)
    family_name: TextField = TextField(null=False)
    birthdate: DateField = DateField(null=False)
    gender: TextField = TextField(null=False)
    score_father = FloatField(default=0, null=False)
    score_mother = FloatField(default=0, null=False)
    is_supervised = BooleanField(default=False, null=False)
    sick = BooleanField(default=False, null=False)
    mentalage = FloatField(null=True)
    saved = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'autistes'
        unique_together = (('parent_id', 'name', 'birthdate'),)


class Level1(Model):
    patient = ForeignKey(to='Autiste', on_delete=SET_NULL, null=True)
    type_parent = CharField(null=False, max_length=10, choices=(('mother', 'mother'), ('father', 'father')))
    parent = ForeignKey(to=user_model, on_delete=CASCADE, null=False)
    looks_at_pointed_item = TextField(null=False, db_column='looks_at_pointed_item')
    possibly_deaf = TextField(null=False, db_column='possibly_deaf')
    pretending_playing = TextField(null=False, db_column='pretending_playing')
    climbing_things = TextField(null=False, db_column='climbing_things')
    unusual_moves_next_to_eyes = TextField(null=False, db_column='unusual_moves_next_to_eyes')
    point_to_get_assistance = TextField(null=False, db_column='point_to_get_assistance')
    point_to_show_smth = TextField(null=False, db_column='point_to_show_smth')
    cares_abt_other_children = TextField(null=False, db_column='cares_abt_other_children')
    bring_smth_to_show = TextField(null=False, db_column='bring_smth_to_show')
    response_to_his_name = TextField(null=False, db_column='response_to_his_name')
    smiles_back = TextField(null=False, db_column='smiles_back')
    annoyed_by_daily_noise = TextField(null=False, db_column='annoyed_by_daily_noise')
    walks = TextField(null=False, db_column='walks')
    makes_eye_contact = TextField(null=False, db_column='makes_eye_contact')
    imitate_parent_action = TextField(null=False, db_column='imitate_parent_action')
    turn_head_like_parent = TextField(null=False, db_column='turn_head_like_parent')
    make_parent_watch = TextField(null=False, db_column='make_parent_watch')
    understand_assignments = TextField(null=False, db_column='understand_assignments')
    check_parent_reaction = TextField(null=False, db_column='check_parent_reaction')
    loves_dynamic_activities = TextField(null=False, db_column='loves_dynamic_activities')

    class Meta:
        db_table = 'level1'


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
    patient = AutisteSerializer()
    doctor = UserSerializer()

    class Meta:
        model = Supervise
        fields = "__all__"


class ConsultationSerializer(ModelSerializer):
    patient = AutisteSerializer()
    doctor = UserSerializer()

    class Meta:
        model = Consultation
        fields = '__all__'


class Level1serializer(ModelSerializer):
    class Meta:
        model = Level1
        fields = '__all__'
