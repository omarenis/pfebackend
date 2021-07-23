from django.urls import path

from common.models import text_field
from common.views import FormViewSet, ViewSet
from formteacher.models import BehaviorTroubleTeacherSerializer, ExtraTroubleTeacherSerializer, \
    HyperActivityTroubleTeacherSerializer, \
    ImpulsivityTroubleTeacherSerializer, InattentionTroubleTeacherSerializer
from formteacher.services import BehaviorTroubleTeacherService, ExtraTroubleTeacherService, \
    HyperActivityTroubleTeacherService, ImpulsivityTroubleTeacherService, InattentionTroubleTeacherService

behavior_trouble_teacher_fields = {
    'arrogant_impolite': text_field,
    'angry_unexpected_behavior': text_field,
    'sensitive_criticism': text_field,
    'pout_sulk_easily': text_field,
    'moody': text_field,
    'brawler': text_field,
    'deny_mistakes_blame_others': text_field
}

impulsivity_trouble_teacher_fields = {
    'restless_squirms_chair': text_field,
    'unappropriate_noices': text_field,
    'immediately_satisfied_needs': text_field,
    'annoy_students': text_field,
    'go_right_left': text_field,
    'easily_turn_on_impulsive': text_field,
    'excessive_attention_from_teacher': text_field
}

extra_trouble_teacher = {
    'submissive_attitude_towards_authority': text_field,
    'less_accepted_by_group': text_field,
    'Trouble_integrating_with_other_students': text_field,
    'less_cooperate_with_classmates': text_field
}

inattention_trouble_teacher = {
    'distracted': text_field,
    'dreamer': text_field,
    'be_led_by_others': text_field,
    'Trouble_guiding_others': text_field,
    'immature': text_field,
    'easily_upset_make_effort': text_field
}

hyperactivity_trouble_teacher = {
    'restless_squirms_chair': text_field,
    'distracted': text_field,
    'annoy_students': text_field,
    'pout_sulk_easily': text_field,
    'moody': text_field
}


class BehaviorTroubleTeacherViewSet(FormViewSet):
    def __init__(self, fields=None, serializer_class=BehaviorTroubleTeacherSerializer,
                 service=BehaviorTroubleTeacherService(), **kwargs):
        if fields is None:
            fields = behavior_trouble_teacher_fields
        super().__init__(fields, serializer_class, service, **kwargs)


class HyperActivityTroubleTeacherViewSet(FormViewSet):
    def __init__(self, fields=None, serializer_class=HyperActivityTroubleTeacherSerializer,
                 service=HyperActivityTroubleTeacherService(), **kwargs):
        if fields is None:
            fields = hyperactivity_trouble_teacher
        super().__init__(fields, serializer_class, service, **kwargs)


class ImpulsivityTroubleTeacherViewSet(FormViewSet):
    def __init__(self, fields=None, serializer_class=ImpulsivityTroubleTeacherSerializer,
                 service=ImpulsivityTroubleTeacherService(), **kwargs):
        if fields is None:
            fields = impulsivity_trouble_teacher_fields
        super().__init__(fields, serializer_class, service, **kwargs)


class ExtraTroubleTeacherViewSet(FormViewSet):
    def __init__(self, fields=None, serializer_class=ExtraTroubleTeacherSerializer,
                 service=ExtraTroubleTeacherService(), **kwargs):
        if fields is None:
            fields = extra_trouble_teacher
        super().__init__(fields, serializer_class, service, **kwargs)


class InattentionTroubleTeacherViewSet(ViewSet):
    def __init__(self, fields=None, serializer_class=InattentionTroubleTeacherSerializer,
                 service=InattentionTroubleTeacherService(), **kwargs):
        if fields is None:
            fields = inattention_trouble_teacher
        super().__init__(fields, serializer_class, service, **kwargs)


behavior_trouble_teacher_list = BehaviorTroubleTeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

behavior_trouble_teacher_object = BehaviorTroubleTeacherViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

impulsivity_trouble_teacher_list = ImpulsivityTroubleTeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

impulsivity_trouble_teacher_object = ImpulsivityTroubleTeacherViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})


hyperactivity_trouble_teacher_list = HyperActivityTroubleTeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

hyperactivity_trouble_teacher_object = HyperActivityTroubleTeacherViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

extra_trouble_teacher_list = ExtraTroubleTeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

extra_trouble_teacher_object = ExtraTroubleTeacherViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

inattention_trouble_teacher_list = InattentionTroubleTeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

inattention_trouble_teacher_object = InattentionTroubleTeacherViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'delete'
})

urlpatterns = [
    path('behavior_trouble_teacher_list', behavior_trouble_teacher_list),
    path('behavior_trouble_teacher_list/<int:id>', behavior_trouble_teacher_object),
    path('impulsivity_trouble_teacher_list', impulsivity_trouble_teacher_list),
    path('impulsivity_trouble_teacher_list/<int:id>', impulsivity_trouble_teacher_list),
    path('hyperactivity_trouble_teacher_list', hyperactivity_trouble_teacher_list),
    path('hyperactivity_trouble_teacher_list/<int:id>', hyperactivity_trouble_teacher_object),
    path('extra_trouble_teacher_list', extra_trouble_teacher_list),
    path('extra_trouble_teacher_list/<int:id>', extra_trouble_teacher_object),
    path('inattention_trouble_teacher_list', inattention_trouble_teacher_list),
    path('inattention_trouble_teacher_list/<int:id>', inattention_trouble_teacher_object)
]
