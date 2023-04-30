from typing import Union

from common.repositories import Repository
from .models import Localisation, User


class UserRepository(Repository):
    def __init__(self, model=User):
        super().__init__(model)


class LocalisationRepository(Repository):
    def __init__(self, model=Localisation):
        super().__init__(model)
