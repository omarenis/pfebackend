from common.models import text_field
from common.services import Service
from .repositories import BehaviorTroubleTeacherRepository, HyperActivityTroubleTeacherRepository, \
    InattentionTroubleTeacherRepository, FormAbrTeacherRepository, BehaviorTroubleParentRepository, \
    LearningTroubleParentRepository, SomatisationTroubleParentRepository, FormAbrParentRepository, \
    AnxityTroubleParentRepository, HyperActivityTroubleParentRepository

BEHAVIOR_TROUBLE_TEACHER_FIELDS = {
    # 4-5-6-10-11-12-23-27
    'arrogant_impolite': text_field,
    'angry_unexpected_behavior': text_field,
    'sensitive_criticism': text_field,
    'pout_sulk_easily': text_field,
    'moody': text_field,
    'brawler': text_field,
    'deny_mistakes_blameOthers': text_field,
    'few_relation_school': text_field,
}

HYPER_ACTIVITY_TROUBLE_Teacher = {
    # 1-2-3-8-14-15-16
    'restless_squirms_chair': text_field,
    'inappropriate_noises': text_field,
    'immediately_satisfied_needs': text_field,
    'annoy_students': text_field,
    'goes_left_right': text_field,
    'easily_turn_on_impulsive': text_field,
    'excessive_attention_from_teacher': text_field
}

INATTENTION_Trouble_TEACHER = {
    # 7-9-18-20-21-22-26-28
    'distracted': text_field,
    'dreamer': text_field,
    'led_by_others': text_field,
    'trouble_guiding_others': text_field,
    'trouble_finishing_things': text_field,
    'immature': text_field,
    'upset_easily_make_effort': text_field,
    'has_learning_difficulties': text_field,
}

FORM_ABR_Teacher = {
    # 1-5-7-8-10-11-14-15-21-26
    'restless_squirms_chair': text_field,
    'angry_unexpected_behavior': text_field,
    'distracted': text_field,
    'annoy_students': text_field,
    'pout_sulk_easily': text_field,
    'moody': text_field,
    'goes_left_right': text_field,
    'easily_turn_on_impulsive': text_field,
    'trouble_finishing_things': text_field,
    'upset_easily_make_effort': text_field
}

BEHAVIOR_TROUBLE_PARENTS = {
    'insolent_with_grown_ups': text_field,
    'feels_attacked_defensive': text_field,
    'destructive': text_field,
    'deny_mistakes_blame_others': text_field,
    'quarrelsome_get_involved_fight': text_field,
    'bully_intimidate_comrades': text_field,
    'constantly_fight': text_field,
    'unhappy': text_field
}
LEARNING_TROUBLE_PARENT_FIELDS = {
    'has_learning_difficulties': text_field,
    'trouble_finishing_things': text_field,
    'easily_being_distracted': text_field,
    'enability_finish_when_do_effort': text_field
}
SOMATISATION_TROUBLE_PARENT_FIELDS = {
    'headaches': text_field,
    'upset_stomach': text_field,
    'physical_aches': text_field,
    'vomiting_nausea': text_field
}

HYPERACTIVITY_TROUBLE_PARENT_FIELDS = {
    'excitable_impulsive': text_field,
    'want_dominate': text_field,
    'squirms': text_field,
    'restless_needs_do_something': text_field}

ANXITY_TROUBLE_PARENT_FIELDS = {
    'afraid_new_things': text_field,
    'shy': text_field,
    'worry_much': text_field,
    'being_crashed_manipulated': text_field
}

FORM_ABR_PARENT_FIELDS = {
    'excitable_impulsive': text_field,
    'cry_often_easily': text_field,
    'squirms': text_field,
    'restless_needs_do_something': text_field,
    'destructive': text_field,
    'trouble_finishing_things': text_field,
    'easily_being_distracted': text_field,
    'moody': text_field,
    'enability_finish_when_do_effort': text_field,
    'disturb_other_children': text_field
}


class BehaviorTroubleTeacherService(Service):
    def __init__(self, repository=BehaviorTroubleTeacherRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_TEACHER_FIELDS)


class HyperActivityTroubleTeacherService(Service):
    def __init__(self, repository=HyperActivityTroubleTeacherRepository()):
        super().__init__(repository, fields=HYPER_ACTIVITY_TROUBLE_Teacher)


class InattentionTroubleTeacherService(Service):
    def __init__(self, repository=InattentionTroubleTeacherRepository()):
        super().__init__(repository, fields=INATTENTION_Trouble_TEACHER)


class FormAbrTeacherService(Service):

    def __init__(self, repository=FormAbrTeacherRepository()):
        super().__init__(repository, fields=FORM_ABR_Teacher)


class BehaviorTroubleParentService(Service):
    def __init__(self, repository=BehaviorTroubleParentRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_PARENTS)


class LearningTroubleParentService(Service):
    def __init__(self, repository=LearningTroubleParentRepository()):
        super().__init__(repository, fields=LEARNING_TROUBLE_PARENT_FIELDS)


class SomatisationTroubleParentService(Service):
    def __init__(self, repository=SomatisationTroubleParentRepository()):
        super().__init__(repository, fields=SOMATISATION_TROUBLE_PARENT_FIELDS)


class HyperActivityTroubleParentService(Service):
    def __init__(self, repository=HyperActivityTroubleParentRepository()):
        super().__init__(repository, fields=HYPERACTIVITY_TROUBLE_PARENT_FIELDS)


class AnxityTroubleParentService(Service):
    def __init__(self, repository=AnxityTroubleParentRepository()):
        super().__init__(repository, fields=ANXITY_TROUBLE_PARENT_FIELDS)


class FormAbrParentService(Service):
    def __init__(self, repository=FormAbrParentRepository()):
        super().__init__(repository, fields=FORM_ABR_PARENT_FIELDS)
