from django.urls import path
from common.views import ViewSet
from tdah.models import BehaviorTroubleTeacherSerializer, HyperActivityTroubleTeacherSerializer, \
    InattentionTroubleTeacherSerializer, FormAbrSerializer, BehaviorTroubleParentSerializer, \
    LearningTroubleParentSerializer, SomatisationTroubleParentSerializer, HyperActivityTroubleParentSerializer, \
    AnxityTroubleParentSerializer, FormAbrParentSerializer
from tdah.services import BehaviorTroubleTeacherService, HyperActivityTroubleTeacherService, \
    InattentionTroubleTeacherService, FormAbrTeacherService, BehaviorTroubleParentService, LearningTroubleParentService, \
    SomatisationTroubleParentService, HyperActivityTroubleParentService, AnxityTroubleParentService, \
    FormAbrParentService


# Create your views here.

class BehaviorTroubleTeacherViewSet(ViewSet):
    def __init__(self, serializer_class=BehaviorTroubleTeacherSerializer, service=BehaviorTroubleTeacherService(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class HyperActivityTroubleTeacherViewSet(ViewSet):
    def __init__(self, serializer_class=HyperActivityTroubleTeacherSerializer,
                 service=HyperActivityTroubleTeacherService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class InattentionTroubleTeacherViewSet(ViewSet):
    def __init__(self, serializer_class=InattentionTroubleTeacherSerializer,
                 service=InattentionTroubleTeacherService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class FormAbrTeacherViewSet(ViewSet):
    def __init__(self, serializer_class=FormAbrSerializer, service=FormAbrTeacherService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class BehaviorTroubleParentViewSet(ViewSet):
    def __init__(self, serializer_class=BehaviorTroubleParentSerializer, service=BehaviorTroubleParentService(),
                 **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class LearningTroubleParentViewSet(ViewSet):
    def __init__(self, serializer_class=LearningTroubleParentSerializer,
                 service=LearningTroubleParentService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class SomatisationTroubleParentViewSet(ViewSet):
    def __init__(self, serializer_class=SomatisationTroubleParentSerializer,
                 service=SomatisationTroubleParentService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class HyperActivityTroubleParentViewSet(ViewSet):
    def __init__(self, serializer_class=HyperActivityTroubleParentSerializer,
                 service=HyperActivityTroubleParentService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class AnxityTroubleParentViewSet(ViewSet):
    def __init__(self, serializer_class=AnxityTroubleParentSerializer,
                 service=AnxityTroubleParentService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


class FormAbrParentViewSet(ViewSet):
    def __init__(self, serializer_class=FormAbrParentSerializer,
                 service=FormAbrParentService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)


behavior_trouble_parent_list, behavior_trouble_parent_object = BehaviorTroubleParentViewSet.get_urls()

learning_trouble_parent_list, learning_trouble_parent_object = LearningTroubleParentViewSet.get_urls()

somatisation_trouble_parent_list, somatisation_trouble_parent_object = SomatisationTroubleParentViewSet.get_urls()

hyperactivity_trouble_parent_list, hyperactivity_trouble_parent_object = HyperActivityTroubleParentViewSet.get_urls()

anxity_trouble_parent_list, anxity_trouble_parent_object = AnxityTroubleParentViewSet.get_urls()

form_abr_parent_list, form_abr_parent_object = FormAbrParentViewSet.get_urls()


behavior_trouble_teacher_list, behavior_trouble_teacher_object = BehaviorTroubleTeacherViewSet.get_urls()

hyperactivity_trouble_teacher_list, hyperactivity_trouble_teacher_object = HyperActivityTroubleTeacherViewSet.get_urls()

inattention_trouble_teacher_list, inattention_trouble_teacher_object = InattentionTroubleTeacherViewSet.get_urls()

form_abr_teacher_list, form_abr_teacher_object = FormAbrTeacherViewSet.get_urls()

urlpatterns = [
    path('behavior_trouble_teacher_list', behavior_trouble_teacher_list),
    path('behavior_trouble_teacher_list/<int:id>', behavior_trouble_teacher_object),
    path('hyperactivity_trouble_teacher_list', hyperactivity_trouble_teacher_list),
    path('hyperactivity_trouble_teacher_list/<int:id>', hyperactivity_trouble_teacher_object),
    path('inattention_trouble_teacher_list', inattention_trouble_teacher_list),
    path('inattention_trouble_teacher_list/<int:id>', inattention_trouble_teacher_object),
    path('form_abr', form_abr_teacher_list),
    path('form_abr/<int:id>', form_abr_teacher_object),
    path('behavior_trouble_parent_list', behavior_trouble_parent_list),
    path('behavior_trouble_parent_list/<int:id>', behavior_trouble_parent_object),

    path('learning_trouble_parent_list', learning_trouble_parent_list),
    path('learning_trouble_parent_list/<int:id>', learning_trouble_parent_object),

    path('somatisation_trouble_parent_list', somatisation_trouble_parent_list),
    path('somatisation_trouble_parent_list/<int:id>', somatisation_trouble_parent_object),

    path('hyperactivity_trouble_parent_list', hyperactivity_trouble_parent_list),
    path('hyperactivity_trouble_parent_list/<int:id>', hyperactivity_trouble_parent_object),

    path('anxity_trouble_parent_list', anxity_trouble_parent_list),
    path('anxity_trouble_parent_list/<int:id>', anxity_trouble_parent_object),

    path('form_abr_parent_list', form_abr_parent_list),
    path('form_abr_parent_list/<int:id>', form_abr_parent_object)
]
