from django.db import models
from rest_framework.serializers import ModelSerializer


class Email(models.Model):
    sender: models.EmailField = models.EmailField(null=False)
    subject: models.TextField = models.TextField(null=False)
    content: models.TextField = models.TextField(null=False)

    class Meta:
        db_table = "messages"


class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


