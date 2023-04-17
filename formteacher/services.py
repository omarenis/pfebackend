from common.models import text_field
from common.services import FormService
from .repositories import BehaviorTroubleTeacherRepository, HyperActivityTroubleTeacherRepository, \
    InattentionTroubleTeacherRepository, FormAbrTeacherRepository

BEHAVIOR_TROUBLE_TEACHER_FIELDS = {
    # 4-5-6-10-11-12-23-27
    'arrogantImpolite': text_field,
    'angryUnexpectedBehavior': text_field,
    'sensitiveCriticism': text_field,
    'poutSulkEasily': text_field,
    'moody': text_field,
    'brawler': text_field,
    'denyMistakesBlameOthers': text_field,
    'fewRelationSchool': text_field,
}

HYPER_ACTIVITY_TROUBLE_Teacher = {
    # 1-2-3-8-14-15-16
    'restlessSquirmsChair': text_field,
    'inappropriateNoises': text_field,
    'immediatelySatisfiedNeeds': text_field,
    'annoyStudents': text_field,
    'goesLeftRight': text_field,
    'easilyTurnOnImpulsive': text_field,
    'excessiveAttentionFromTeacher': text_field
}

INATTENTION_Trouble_TEACHER = {
    # 7-9-18-20-21-22-26-28
    'distracted': text_field,
    'dreamer': text_field,
    'ledByOthers': text_field,
    'troubleGuidingOthers': text_field,
    'troubleFinishingThings': text_field,
    'immature': text_field,
    'upsetEasilyMakeEffort': text_field,
    'hasLearningDifficulties': text_field,
}

FORM_ABR_Teacher = {
    # 1-5-7-8-10-11-14-15-21-26
    'restlessSquirmsChair': text_field,
    'angryUnexpectedBehavior': text_field,
    'distracted': text_field,
    'annoyStudents': text_field,
    'poutSulkEasily': text_field,
    'moody': text_field,
    'goesLeftRight': text_field,
    'easilyTurnOnImpulsive': text_field,
    'troubleFinishingThings': text_field,
    'upsetEasilyMakeEffort': text_field
}


class BehaviorTroubleTeacherService(FormService):
    def __init__(self, repository=BehaviorTroubleTeacherRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_TEACHER_FIELDS)


class HyperActivityTroubleTeacherService(FormService):
    def __init__(self, repository=HyperActivityTroubleTeacherRepository()):
        super().__init__(repository)


class InattentionTroubleTeacherService(FormService):
    def __init__(self, repository=InattentionTroubleTeacherRepository()):
        super().__init__(repository)


class InattentionTroubleTeacherService(FormService):
    def __init__(self, repository=InattentionTroubleTeacherRepository()):
        super().__init__(repository, fields=INATTENTION_Trouble_TEACHER)


class FormAbrTeacherService(FormService):

    def __init__(self, repository=FormAbrTeacherRepository()):
        super().__init__(repository, fields=FORM_ABR_Teacher)
