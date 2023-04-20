from typing import Union

from common.repositories import Repository
from .models import Localisation, Parent, Teacher


class UserRepository(Repository):
    def __init__(self, model=Union[Parent, Teacher]):
        super().__init__(model)


class LocalisationRepository(Repository):
    def __init__(self, model=Localisation):
        super().__init__(model)
