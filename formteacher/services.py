from common.models import text_field
from common.services import FormService
from .repositories import BehaviorTroubleTeacherRepository, HyperActivityTroubleTeacherRepository, \
    InattentionTroubleTeacherRepository, FormAbrTeacherRepository

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


class BehaviorTroubleTeacherService(FormService):
    def __init__(self, repository=BehaviorTroubleTeacherRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_TEACHER_FIELDS)


class HyperActivityTroubleTeacherService(FormService):
    def __init__(self, repository=HyperActivityTroubleTeacherRepository()):
        super().__init__(repository, fields=HYPER_ACTIVITY_TROUBLE_Teacher)


class InattentionTroubleTeacherService(FormService):
    def __init__(self, repository=InattentionTroubleTeacherRepository()):
        super().__init__(repository, fields=INATTENTION_Trouble_TEACHER)


class FormAbrTeacherService(FormService):

    def __init__(self, repository=FormAbrTeacherRepository()):
        super().__init__(repository, fields=FORM_ABR_Teacher)
