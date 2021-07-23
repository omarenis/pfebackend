from django.urls import path

from common.models import text_field
from common.views import ViewSet
from formparent.models import AnxityTroubleParentSerializer, ExtraTroubleParentSerializer, \
    HyperActivityTroubleParentSerializer, ImpulsivityTroubleParentSerializer, \
    LearningTroubleParentSerializer, SomatisationTroubleParentSerializer
from formparent.services import AnxityTroubleParentService, ExtraTroubleParentService, \
    HyperActivityTroubleParentService, ImpulsivityTroubleParentService, \
    LearningTroubleParentService, SomatisationTroubleParentService

ANXITY_TROUBLE_PARENT_FIELDS = {
    'afraid_environment': text_field,
    'shy': text_field,
    'worry_much': text_field,
    'being_crashed_manipulated': text_field
}

IMPULSIVITY_TROUBLE_PARENT_FIELD = {
    'excitable_impulsif': text_field,
    'control_everything': text_field,
    'squirms': text_field,
    'restless_needs_do_something': text_field
}

LEARNING_TROUBLE_PARENT_FIELDS = {
    'has_learning_difficuties': text_field,
    'not_complete_what_started': text_field,
    'easily_disctracted': text_field,
    'discouraged_when_effort_required': text_field
}

SOMATISATION_TROUBLE_PARENT_FIELDS = {
    'headaches': text_field,
    'upset_stomach': text_field,
    'physical_aches': text_field,
    'vomiting_nausea': text_field
}


HYPERACTIVITY_TROUBLE_PARENT_FIELDS = {
    'excitable_impulsif': text_field,
    'cry_often_easily': text_field,
    'squirms': text_field,
    'restless_needs_do_something': text_field,
    'desctructive': text_field,
    'not_complete_what_started': text_field,
    'easily_distracted': text_field,
    'moody': text_field,
    'discouraged_when_effort_required': text_field,
    'disrurb_other_children': text_field
}


EXTRA_TROUBLE_PARENT_FIELDS = {
    'chewing_mibbing_things': text_field,
    'trouble_make_keep_friends': text_field,
    'suck_chew_things': text_field,
    'dreamer': text_field,
    'lie_made_up_stories': text_field,
    'get_troubles_more_than_others': text_field,
    'speak_like_baby_stutters': text_field,
    'pout_sulk': text_field,
    'disobey_reluctantly_obey': text_field,
    'easily_wrinkled_easily_angry': text_field,
    'cannot_stop_during_repetitive_activity': text_field,
    'cruel': text_field,
    'immature': text_field,
    'break_rules': text_field,
    'not_get_along_with_brothers': text_field,
    'feeding_problems': text_field,
    'sleeping_problems': text_field,
    'feel_wronged_cry_out_injustice': text_field,
    'brags_boastful': text_field,
    'bowel_movement_problems': text_field
}


class AnxityTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=AnxityTroubleParentSerializer,
                 service=AnxityTroubleParentService, **kwargs):
        if fields is None:
            fields = ANXITY_TROUBLE_PARENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


class ImpulsivityTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=ImpulsivityTroubleParentSerializer,
                 service=ImpulsivityTroubleParentService, **kwargs):
        if fields is None:
            fields = IMPULSIVITY_TROUBLE_PARENT_FIELD
        super().__init__(fields, serializer_class, service, **kwargs)


class LearningTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=LearningTroubleParentSerializer,
                 service=LearningTroubleParentService(), **kwargs):
        if fields is None:
            fields = LEARNING_TROUBLE_PARENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


class SomatisationTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=SomatisationTroubleParentSerializer,
                 service=SomatisationTroubleParentService(), **kwargs):
        if fields is None:
            fields = SOMATISATION_TROUBLE_PARENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


class HyperActivityTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=HyperActivityTroubleParentSerializer,
                 service=HyperActivityTroubleParentService(), **kwargs):
        if fields is None:
            fields = HYPERACTIVITY_TROUBLE_PARENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


class ExtraTroubleParentViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=ExtraTroubleParentSerializer,
                 service=ExtraTroubleParentService(), **kwargs):
        if fields is None:
            fields = EXTRA_TROUBLE_PARENT_FIELDS
        super().__init__(fields, serializer_class, service, **kwargs)


anxity_trouble_parent_list = AnxityTroubleParentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


anxity_trouble_parent_object = AnxityTroubleParentViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})


urlpatterns = [
    path('anxity_trouble_parent_list', anxity_trouble_parent_list),
    path('anxity_trouble_parent_list/<int:id>', anxity_trouble_parent_object),
]
