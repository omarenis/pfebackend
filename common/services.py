from .repositories import Repository


class Service(object):

    def __init__(self, repository: Repository, fields: dict):
        self.repository = repository
        self.fields = fields

    def list(self): 
        return self.repository.list()

    def retrieve(self, _id: int):
        return self.repository.retrieve(_id=_id)

    def get_by(self, data: dict):
        try:
            return self.repository.model.objects.get(**data)
        except self.repository.model.DoesNotExist:
            return None

    def create(self, data: dict):
        print(data)
        for i in self.fields:
            if data.get(i) is None and self.fields[i].get('required') is True:
                return ValueError(f'{i} must not be null')
        return self.repository.create(data)

    def put(self, _id: int, data: dict):
        return self.repository.put(_id=_id, data=data)

    def delete(self, _id: int):
        return self.repository.delete(_id)

    def filter_by(self, data: dict):
        filter_params = {}
        for i in data:
            if self.fields.get(i) is not None and self.fields.get(i).get('type') == 'text':
                filter_params[f'{i}__contains'] = data[i]
            else:
                filter_params[i] = data[i]
        return self.repository.filter_by(data=filter_params)


def calculate_score(data):
    value = 0
    for i in data:
        if data.get(i) == 'sometimes':
            value += 1
        elif data.get(i) == 'usual':
            value += 2
        elif data.get(i) == 'always':
            value += 3

    return value


def autismelvl1(data, instance):
    value = 0
    for i in data:
        setattr(instance, i, data[i])
        if data.get(i) == 'sucess':
            value += 1
    return value, instance
