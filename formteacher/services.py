from common.services import Service
from .repositories import BehaviorTroubleTeacherRepository, ExtraTroubleTeacherRepository, \
    HyperActivityTroubleTeacherRepository, \
    ImpulsivityTroubleTeacherRepository, InattentionTroubleTeacherRepository


class BehaviorTroubleTeacherService(Service):
    def __init__(self, repository=BehaviorTroubleTeacherRepository()):
        super().__init__(repository)


class HyperActivityTroubleTeacherService(Service):
    def __init__(self, repository=HyperActivityTroubleTeacherRepository()):
        super().__init__(repository)


class ImpulsivityTroubleTeacherService(Service):
    def __init__(self, repository=ImpulsivityTroubleTeacherRepository()):
        super().__init__(repository)


class ExtraTroubleTeacherService(Service):
    def __init__(self, repository=ExtraTroubleTeacherRepository()):
        super().__init__(repository)


class InattentionTroubleTeacherService(Service):
    def __init__(self, repository=InattentionTroubleTeacherRepository()):
        super().__init__(repository)
