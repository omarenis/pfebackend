from django.db.models import CASCADE, ForeignKey, Model
from django.db.models.fields import FloatField, TextField
from common.models import create_model_serializer, patient_model_location


class Form(Model):
    patient = ForeignKey(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        abstract = True


class BehaviorTroubleTeacher(Form):
    arrogant_impolite: TextField = TextField(null=False)
    angry_unexpected_behavior: TextField = TextField(null=False)
    sensitive_criticism: TextField = TextField(null=False)
    pout_sulk_easily: TextField = TextField(null=False)
    moody: TextField = TextField(null=False)
    brawler: TextField = TextField(null=False)
    deny_mistakes_blame_others: TextField = TextField(null=False)

    class Meta:
        db_table = 'behavoir_trouble_teacher'


class HyperActivityTroubleTeacher(Form):
    restless_squirms_chair: TextField = TextField(null=False)
    distracted: TextField = TextField(null=False)
    annoy_students: TextField = TextField(null=False)
    pout_sulk_easily: TextField = TextField(null=False)
    moody: TextField = TextField(null=False)
    go_right_left: TextField = TextField(null=False)
    easily_turn_on_impulsive: TextField = TextField(null=False)
    trouble_finishing_things: TextField = TextField(null=False)
    upset_easily_make_effort: TextField = TextField(null=False)

    class Meta:
        db_table = 'hyperactivity_trouble_teacher'


class ImpulsivityTroubleTeacher(Form):
    restless_squirms_chair: TextField = TextField(null=False)
    unappropriate_noices = TextField(null=False)
    immediately_satisfied_needs = TextField(null=False)
    annoy_students = TextField(null=False)
    go_right_left = TextField(null=False)
    easily_turn_on_impulsive = TextField(null=False)
    excessive_attention_from_teacher = TextField(null=False)

    class Meta:
        db_table = 'impulsivity_trouble_teacher'


class ExtraTroubleTeacher(Form):
    submissive_attitude_towards_authority = TextField(null=False, unique=False)
    less_accepted_by_group = TextField(null=False, unique=False)
    Trouble_integrating_with_other_students = TextField(null=False, unique=False)
    less_cooperate_with_classmates = TextField(null=False)

    class Meta:
        db_table = 'extra_trouble_teacher'


class InattentionTroubleTeacher(Form):
    distracted = TextField(null=False)
    dreamer = TextField(null=False)
    be_led_by_others = TextField(null=False)
    Trouble_guiding_others = TextField(null=False)
    Trouble_finishing_things = TextField(null=False)
    immature = TextField(null=False)
    easily_upset_make_effort = TextField(null=False)

    class Meta:
        db_table = 'inattention_trouble_teacher'


BehaviorTroubleTeacherSerializer = create_model_serializer(model=BehaviorTroubleTeacher,
                                                           name='BehaviorTroubleTeacherSerializer')
HyperActivityTroubleTeacherSerializer = create_model_serializer(model=HyperActivityTroubleTeacher,
                                                                name='HyperActivityTroubleTeacherSerializer')

ImpulsivityTroubleTeacherSerializer = create_model_serializer(name="ImpulsivityTroubleTeacherSerializer",
                                                              model=ImpulsivityTroubleTeacher)
ExtraTroubleTeacherSerializer = create_model_serializer(name='ExtraTroubleTeacherSerializer',
                                                        model=ExtraTroubleTeacher)
InattentionTroubleTeacherSerializer = create_model_serializer(name='InattentionTroubleTeacherSerializer',
                                                              model=InattentionTroubleTeacher)
