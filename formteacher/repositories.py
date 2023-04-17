from common.repositories import Repository
from .models import BehaviorTroubleTeacher, HyperActivityTroubleTeacher, InattentionTroubleTeacher, FormAbrTeacher



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
