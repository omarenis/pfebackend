from django.contrib.auth.hashers import check_password
from common.services import Service
from gestionusers.repositories import LocalisationRepository, UserRepository


class LocalisationService(Service):
    def __init__(self, repository=LocalisationRepository()):
        super().__init__(repository)


class PersonService(Service):
    def __init__(self, repository=UserRepository()):
        super().__init__(repository)

    def login(self, email, password):
        user = self.filter_by({'email': email}).first()
        if user is not None:
            if check_password(password=password, encoded=user.password):
                return user
            else:
                return Exception('كلمة السر غير صحيحة')
        else:
            return Exception('الحساب غير موجود')
