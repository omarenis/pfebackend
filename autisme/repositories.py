from .models import Level1
from common.repositories import Repository


class Level1repository(Repository):
    def __init__(self, model=Level1):
        super().__init__(model)
