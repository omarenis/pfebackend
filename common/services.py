import json

from .repositories import Repository
from django.core.exceptions import ObjectDoesNotExist

class Service(object):

    def verify_required_data(self, data: dict):
        for i in self.fields:
            if data.get(i) is None and self.fields[i].get('required') is True:
                raise ValueError(f'{i} must not be null')
            if self.fields.get(i).get('type') == 'foreign_key' and data.get(i) is not None:
                data[f'{i}_id'] = data.pop(i)
            elif self.fields[i].get('type') == 'slug':
                if self.fields[i].get('field_to_slug') is None:
                    raise ValueError('field to slug must be not None')
                data[i] = slugify(data[self.fields[i].get('field_to_slug')])
            elif self.fields[i].get('unique') is True:
                try:
                    self.repository.retrieve({i: data.get(i)})
                    raise ValueError(f'{i} is unique')
                except self.repository.model.DoesNotExist:
                    continue
        return data

    def verify_data(self, data: dict):
        raw = {}

        for i in data:
            if self.fields.get(i) is None:
                raise AttributeError(f'{i} is not an attribute on the model')
            else:
                    if self.fields.get(i).get('type') == 'foreign_key':
                        model = self.fields.get(i).get('classMap')
                        try:
                            raw[i] = model.objects.get(id=data[i])
                        except model.DoesNotExist:
                            raise ObjectDoesNotExist(f'{i} with id = {data[i]} does not exist')
                    else:
                        raw[i] = data[i]
        return raw

    def __init__(self, repository: Repository, fields: dict):
        self.repository = repository
        self.fields = fields

    def list(self):
        return self.repository.list()

    def retrieve(self, pk: int):
        return self.repository.retrieve(_id=pk)

    def create(self, data: dict):
        self.verify_required_data(data)
        return self.repository.create(data)

    def put(self, pk: int, data: dict):
        data = self.verify_data(data)
        return self.repository.put(pk=pk, data=data)

    def delete(self, pk: int):
        return self.repository.delete(pk)

    def filter_by(self, data: dict):
        filter_params = {}
        for i in data:
            if self.fields.get(i) is not None and self.fields.get(i).get('type') == 'text':
                filter_params[f'{i}__contains'] = data[i]
            filter_params[i] = data[i]
        return self.repository.filter_by(data=filter_params)

    def import_data(self, data: list):
        for row in data:
            instanceData = {}
            for i in self.fields:
                if self.fields[i].get('type') == 'file':
                    instanceData[i] = SimpleUploadedFile(name=str(URI(str(row[i])).path).split('/')[-1],
                                                         content=urlopen(url=str(data.get(i))).read())
                elif self.fields[i].get('type') == 'date' or self.fields[i].get('type') == 'datetime':
                    instanceData[i] = datetime.datetime.fromisoformat(data[i])
                elif self.fields[i].get('type') == 'foreign_key':
                    try:
                        instanceData[f'{i}__id'] = int(data.pop(i))
                    except ValueError:
                        instance, _ = self.fields.get(i).get('classMap').objects.get_or_create(
                            **json.loads(str(row.pop(i))))
                else:
                    instanceData[i] = str(row[i])
            self.create(instanceData)

    def export_data(self):
        output = {}
        data = self.repository.list()
        for row in data:
            for field in self.fields:
                if output.get(field) is None:
                    if self.fields.get(field).get('type') == 'int':
                        value = int(getattr(row, field))
                    elif self.fields.get(field).get('type') == 'float':
                        value = float(getattr(row, field))
                    elif self.fields.get(field).get('type') == 'file':
                        value = str(getattr(getattr(data, field), 'url'))
                    else:
                        value = str(getattr(row, field))


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
