from .repositories import Repository
<<<<<<< HEAD


class Service(object):

    def __init__(self, repository: Repository):
        self.repository = repository
=======
from gestionpatient.models import Patient
from gestionusers.models import User
from matrices import matrix
class Service(object):

    def __init__(self, repository: Repository, fields: dict):
        self.repository = repository
        self.fields = fields
>>>>>>> origin/main

    def list(self):
        return self.repository.list()

<<<<<<< HEAD
    def retreive(self, _id: int):
        return self.repository.retreive(_id=_id)

    def create(self, data: dict):
=======
    def retrieve(self, _id: int):
        return self.repository.retrieve(_id=_id)

    def create(self, data: dict):
        print(data)
        for i in self.fields:
            if data.get(i) is None and self.fields[i].get('required') is True:
                return ValueError(f'{i} must not be null')
>>>>>>> origin/main
        return self.repository.create(data)

    def put(self, _id: int, data: dict):
        return self.repository.put(_id=_id, data=data)

    def delete(self, _id: int):
        return self.repository.delete(_id)

    def filter_by(self, data: dict):
<<<<<<< HEAD
        return self.repository.filter_by(data=data)


class FormService(Service):
    def __init__(self, repository: Repository):
        super().__init__(repository)

    def create(self, data: dict):
        try:
            data['score'] = calculate_score(data=data, fields=list(data.keys()))
            return super().create(data=data)
        except Exception as exception:
            return exception
=======
        filter_params = {}
        for i in data:
            if self.fields.get(i) is not None and self.fields.get(i).get('type') == 'text':
                filter_params[f'{i}__contains'] = data[i]
            filter_params[i] = data[i]
        return self.repository.filter_by(data=filter_params)
>>>>>>> origin/main


def calculate_score(data, fields):
    value = 0
<<<<<<< HEAD
    print(data)
=======
>>>>>>> origin/main
    for i in fields:
        if not data.get(i):
            raise AttributeError(f'{i} is not an attribte for the instance')
        elif data.get(i) == 'sometimes':
            value += 1
        elif data.get(i) == 'usual':
            value += 2
        elif data.get(i) == 'always':
            value += 3
    return value
<<<<<<< HEAD
=======

class FormService(Service):
    def __init__(self, repository: Repository, fields):
        super().__init__(repository, fields)

    def create(self, data: dict):
        try:
            patient = Patient.objects.get(id=data['patient_id'])
            user = User.objects.get(id=patient.user_id)
            gender = patient.gender
            tr_age = patient.tr_age

            a=matrix(gender,User.typeUser,tr_age)
            #data['score'] = a[__name__][calculate_score(data=data, fields=list(data.keys()))]
            return super().create(data=data)
        except Exception as exception:
            return exception


>>>>>>> origin/main
