from common.repositories import Repository
from formparent.models import BehaviorTroubleParent, LearningTroubleParent, \
    SomatisationTroubleParent, HyperActivityTroubleParent, AnxityTroubleParent, FormAbrParent


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
