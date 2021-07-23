from common.services import Service
from .repositories import AnxityTroubleParentRepository, BehaviorTroubleParentRepository, \
    ExtraTroubleParentRepository, HyperActivityTroubleParentRepository, \
    ImpulsivityTroubleParentRepository, \
    LearningTroubleParentRepository, SomatisationTroubleParentRepository


class AnxityTroubleParentService(Service):
    def __init__(self, repository=AnxityTroubleParentRepository()):
        super().__init__(repository)


class ImpulsivityTroubleParentService(Service):
    def __init__(self, repository=ImpulsivityTroubleParentRepository()):
        super().__init__(repository)


class LearningTroubleParentService(Service):
    def __init__(self, repository=LearningTroubleParentRepository()):
        super().__init__(repository)


class SomatisationTroubleParentService(Service):
    def __init__(self, repository=SomatisationTroubleParentRepository()):
        super().__init__(repository)


class HyperActivityTroubleParentService(Service):
    def __init__(self, repository=HyperActivityTroubleParentRepository()):
        super().__init__(repository)


class BehaviorTroubleParentService(Service):
    def __init__(self, repository=BehaviorTroubleParentRepository()):
        super().__init__(repository)


class ExtraTroubleParentService(Service):
    def __init__(self, repository=ExtraTroubleParentRepository()):
        super().__init__(repository)
