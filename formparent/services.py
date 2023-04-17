from common.models import text_field
from common.services import FormService
from .repositories import BehaviorTroubleParentRepository, LearningTroubleParentRepository, \
    SomatisationTroubleParentRepository, \
    HyperActivityTroubleParentRepository, AnxityTroubleParentRepository, FormAbrParentRepository

BEHAVIOR_TROUBLE_PARENTS = {
    'insolentWithGrownUps': text_field,
    'feelsAttackedDefensive': text_field,
    'destructive': text_field,
    'denyMistakesBlameOthers': text_field,
    'quarrelsomeGetInvolvedFight': text_field,
    'bullyIntimidateComrades': text_field,
    'constantlyFight': text_field,
    'unhappy': text_field
}
LEARNING_TROUBLE_PARENT_FIELDS = {
    'hasLearningDifficulties': text_field,
    'troubleFinishingThings': text_field,
    'easilyBeingDistracted': text_field,
    'enabilityFinishWhenDoEffort': text_field
}
SOMATISATION_TROUBLE_PARENT_FIELDS = {
    'headaches': text_field,
    'upsetStomach': text_field,
    'physicalAches': text_field,
    'vomitingNausea': text_field
}

HYPERACTIVITY_TROUBLE_PARENT_FIELDS = {
    'excitableImpulsive': text_field,
    'wantDominate': text_field,
    'squirms': text_field,
    'restlessNeedsDoSomething': text_field}

ANXITY_TROUBLE_PARENT_FIELDS = {
    'afraidNewThings': text_field,
    'shy': text_field,
    'worryMuch': text_field,
    'beingCrashedManipulated': text_field
}

FORM_ABR_PARENT_FIELDS = {
    'excitableImpulsive': text_field,
    'cryOftenEasily': text_field,
    'squirms': text_field,
    'restlessNeedsDoSomething': text_field,
    'destructive': text_field,
    'troubleFinishingThings': text_field,
    'easilyBeingDistracted': text_field,
    'moody': text_field,
    'enabilityFinishWhenDoEffort': text_field,
    'disturbOtherChildren': text_field
}


class BehaviorTroubleParentService(FormService):
    def __init__(self, repository=BehaviorTroubleParentRepository()):
        super().__init__(repository, fields=BEHAVIOR_TROUBLE_PARENTS)


class LearningTroubleParentService(FormService):
    def __init__(self, repository=LearningTroubleParentRepository()):
        super().__init__(repository, fields=LEARNING_TROUBLE_PARENT_FIELDS)


class SomatisationTroubleParentService(FormService):
    def __init__(self, repository=SomatisationTroubleParentRepository()):
        super().__init__(repository, fields=SOMATISATION_TROUBLE_PARENT_FIELDS)


class HyperActivityTroubleParentService(FormService):
    def __init__(self, repository=HyperActivityTroubleParentRepository()):
        super().__init__(repository, fields=HYPERACTIVITY_TROUBLE_PARENT_FIELDS)


class AnxityTroubleParentService(FormService):
    def __init__(self, repository=AnxityTroubleParentRepository()):
        super().__init__(repository, fields=ANXITY_TROUBLE_PARENT_FIELDS)


class FormAbrParentService(FormService):
    def __init__(self, repository=FormAbrParentRepository()):
        super().__init__(repository, fields=FORM_ABR_PARENT_FIELDS)
