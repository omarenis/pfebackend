from common.repositories import Repository
from .models import BehaviorTroubleParent, LearningTroubleParent, \
    SomatisationTroubleParent, HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent, BehaviorTroubleTeacher, \
    HyperActivityTroubleTeacher, InattentionTroubleTeacher, FormAbrTeacher


class BehaviorTroubleParentRepository(Repository):
    def __init__(self, model=BehaviorTroubleParent):
        super().__init__(model)


class LearningTroubleParentRepository(Repository):
    def __init__(self, model=LearningTroubleParent):
        super().__init__(model)


class SomatisationTroubleParentRepository(Repository):
    def __init__(self, model=SomatisationTroubleParent):
        super().__init__(model)


class HyperActivityTroubleParentRepository(Repository):
    def __init__(self, model=HyperActivityTroubleParent):
        super().__init__(model)


class AnxityTroubleParentRepository(Repository):
    def __init__(self, model=AnxityTroubleParent):
        super().__init__(model)


class FormAbrParentRepository(Repository):
    def __init__(self, model=FormAbrParent):
        super().__init__(model)


class BehaviorTroubleTeacherRepository(Repository):
    def __init__(self, model=BehaviorTroubleTeacher):
        super().__init__(model)


class HyperActivityTroubleTeacherRepository(Repository):
    def __init__(self, model=HyperActivityTroubleTeacher):
        super().__init__(model)


class InattentionTroubleTeacherRepository(Repository):
    def __init__(self, model=InattentionTroubleTeacher):
        super().__init__(model)


class FormAbrTeacherRepository(Repository):

    def __init__(self, model=FormAbrTeacher):
        super().__init__(model)
