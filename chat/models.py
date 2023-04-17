<<<<<<< HEAD
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


=======
from django.db.models import BooleanField, DateTimeField, Model, TextField
from rest_framework.serializers import ModelSerializer
from django.utils import timezone


class Message(Model):
    sender: TextField = TextField(null=False)
    receivers: TextField = TextField(null=False)
    subject: TextField = TextField(null=False)
    content: TextField = TextField(null=False)
    date: DateTimeField = DateTimeField(null=False, default=timezone.now)
    read: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'messages'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
>>>>>>> origin/main
