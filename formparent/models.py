from django.db.models import CASCADE, FloatField, Model, OneToOneField, TextField
from rest_framework.serializers import ModelSerializer
from common.models import choices, patient_model_location


class ParentForm(Model):
    patient: OneToOneField = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        abstract = True


class AnxityTroubleParent(ParentForm):
    afraid_environment: TextField = TextField(null=False, choices=choices)
    shy: TextField = TextField(null=False, choices=choices)
    worry_much: TextField = TextField(null=False, choices=choices)
    being_crashed_manipulated: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'anxity_trouble_parent'
        abstract = False


class ImpulsivityTroubleParent(ParentForm):
    excitable_impulsif: TextField = TextField(null=False, choices=choices)
    control_everything: TextField = TextField(null=False, choices=choices)
    squirms: TextField = TextField(null=False, choices=choices)
    restless_needs_do_something: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'impulisivity_trouble_parent'
        abstract = False


class LearningTroubleParent(ParentForm):
    has_learning_difficuties: TextField = TextField(null=False, choices=choices)
    not_complete_what_started: TextField = TextField(null=False, choices=choices)
    easily_disctracted: TextField = TextField(null=False, choices=choices)
    discouraged_when_effort_required: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'learning_trouble_parent'
        abstract = False


class SomatisationTroubleParent(ParentForm):
    headaches: TextField = TextField(null=False, choices=choices)
    upset_stomach: TextField = TextField(null=False, choices=choices)
    physical_aches: TextField = TextField(null=False, choices=choices)
    vomiting_nausea: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'somatisation_trouble_parent'
        abstract = False


class HyperActivityTroubleParent(ParentForm):
    excitable_impulsif: TextField = TextField(null=False, choices=choices)
    cry_often_easily: TextField = TextField(null=False, choices=choices)
    squirms: TextField = TextField(null=False, choices=choices)
    restless_needs_do_something: TextField = TextField(null=False, choices=choices)
    desctructive: TextField = TextField(null=False, choices=choices)
    not_complete_what_started: TextField = TextField(null=False, choices=choices)
    easily_distracted: TextField = TextField(null=False, choices=choices)
    moody: TextField = TextField(null=False, choices=choices)
    discouraged_when_effort_required: TextField = TextField(null=False, choices=choices)
    disrurb_other_children: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'hyperactivity_trouble_parent'
        abstract = False


class BehaviorTroubleParent(ParentForm):
    insolent_wth_grown_ups: TextField = TextField(null=False, choices=choices)
    feels_attacked_defensive: TextField = TextField(null=False, choices=choices)
    descructive: TextField = TextField(null=False, choices=choices)
    deny_mistakes_blame_others: TextField = TextField(null=False, choices=choices)
    quarrelsome_get_involved_fight: TextField = TextField(null=False, choices=choices)
    bully_intimidate_comrades: TextField = TextField(null=False, choices=choices)
    constantly_fight: TextField = TextField(null=False, choices=choices)
    unhappy: TextField = TextField(null=False, choices=choices)

    class Meta(ParentForm.Meta):
        db_table = 'behavoir_trouble_parent'
        abstract = False


class ExtraTroubleParent(ParentForm):
    chewing_mibbing_things: TextField = TextField(null=False, choices=choices)
    trouble_make_keep_friends: TextField = TextField(null=False, choices=choices)
    suck_chew_things: TextField = TextField(null=False)
    dreamer: TextField = TextField(null=True)
    lie_made_up_stories: TextField = TextField(null=False)
    get_troubles_more_than_others: TextField = TextField(null=False)
    speak_like_baby_stutters: TextField = TextField(null=False)
    pout_sulk: TextField = TextField(null=False)
    steal_things: TextField = TextField(null=False)
    disobey_reluctantly_obey: TextField = TextField(null=False)
    easily_wrinkled_easily_angry: TextField = TextField(null=False)
    cannot_stop_during_repetitive_activity: TextField = TextField(null=False)
    cruel: TextField = TextField(null=False)
    immature: TextField(null=False)
    break_rules: TextField = TextField(null=False)
    not_get_along_with_brothers: TextField = TextField(null=False)
    feeding_problems: TextField = TextField(null=False)
    sleeping_problems: TextField = TextField(null=False)
    feel_wronged_cry_out_injustice: TextField = TextField(null=False)
    brags_boastful: TextField = TextField(null=False)
    bowel_movement_problems: TextField = TextField(null=False)

    class Meta(ParentForm.Meta):
        db_table = 'extra_trouble_parent'
        abstract = False


class AnxityTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = AnxityTroubleParent
        fields = '__all__'


class ImpulsivityTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = ImpulsivityTroubleParent
        fields = '__all__'


class LearningTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = LearningTroubleParent
        fields = '__all__'


class SomatisationTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = SomatisationTroubleParent
        fields = '__all__'


class HyperActivityTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = HyperActivityTroubleParent
        fields = '__all__'


class BehaviorTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = BehaviorTroubleParent
        fields = '__all__'


class ExtraTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = ExtraTroubleParent
        fields = '__all__'
