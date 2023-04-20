from django.urls import path

from common.models import text_field
from common.views import ViewSet
from formparent.models import BehaviorTroubleParentSerializer, LearningTroubleParentSerializer, \
    SomatisationTroubleParentSerializer, HyperActivityTroubleParentSerializer, AnxityTroubleParentSerializer, \
    FormAbrParentSerializer

from formparent.services import BehaviorTroubleParentService, LearningTroubleParentService, \
    SomatisationTroubleParentService, HyperActivityTroubleParentService, AnxityTroubleParentService, \
    FormAbrParentService


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

urlpatterns = [
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
