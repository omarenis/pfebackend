from common.models import text_field
from common.services import FormService
from .repositories import BehaviorTroubleParentRepository, LearningTroubleParentRepository, \
    SomatisationTroubleParentRepository, \
    HyperActivityTroubleParentRepository, AnxityTroubleParentRepository, FormAbrParentRepository

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


class BehaviorTroubleParentService(FormService):
    def __init__(self, repository=BehaviorTroubleParentRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_PARENTS)


class LearningTroubleParentService(FormService):
    def __init__(self, repository=LearningTroubleParentRepository()):
        super().__init__(repository, fields=LEARNING_TROUBLE_PARENT_FIELDS)


class SomatisationTroubleParentService(FormService):
    def __init__(self, repository=SomatisationTroubleParentRepository()):
        super().__init__(repository, fields=SOMATISATION_TROUBLE_PARENT_FIELDS)


class HyperActivityTroubleParentService(FormService):
    def __init__(self, repository=HyperActivityTroubleParentRepository()):
        super().__init__(repository, fields=HYPERACTIVITY_TROUBLE_PARENT_FIELDS)


class AnxityTroubleParentService(FormService):
    def __init__(self, repository=AnxityTroubleParentRepository()):
        super().__init__(repository, fields=ANXITY_TROUBLE_PARENT_FIELDS)


class FormAbrParentService(FormService):
    def __init__(self, repository=FormAbrParentRepository()):
        super().__init__(repository, fields=FORM_ABR_PARENT_FIELDS)
