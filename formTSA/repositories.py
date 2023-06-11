from common.repositories import Repository
from .models import level1,level2


class level1Repository(Repository):
    def __init__(self, model=level1):
        super().__init__(model)




class level2Repository(Repository):
    def __init__(self, model=level2):
        super().__init__(model)

