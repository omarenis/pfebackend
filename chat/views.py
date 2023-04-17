<<<<<<< HEAD
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.core.mail import send_mail
from django.db import close_old_connections
=======
>>>>>>> origin/main
from django.urls import path
from rest_framework.response import Response
from common.repositories import Repository
from common.services import Service
from common.views import ViewSet
<<<<<<< HEAD
from .models import Email, EmailSerializer
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs


class EmailRepository(Repository):
    def __init__(self, model=Email):
        super().__init__(model)


class EmailService(Service):
    def __init__(self, repository: Repository = EmailRepository()):
        super().__init__(repository)


class MessageViewSet(ViewSet):
    def __init__(self, service=EmailService(), serializer_class=EmailSerializer,
                 required_fields: tuple = ('sender', 'subject', 'content'),
                 fields: tuple = ('sender', 'subject', 'content'), **kwargs):
        super().__init__(service, serializer_class, required_fields, fields, **kwargs)

    def create(self, request, *args, **kwargs):
        sender = request.data.get('sender')
        password = request.data.get('password')
        subject = request.data.get("subject")
        content = request.data.get('content')
        try:
            send_mail(request.data.get('subject'), content, sender, ["omartriki812@gmaiL.com"],
                      fail_silently=False, auth_user=sender, auth_password=password, html_message=content)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=500)
        message = self.service.create({"sender": sender, 'subject': subject, 'content': content})
        if isinstance(message, Exception):
            return Response(data={"error": str(message)}, status=500)
        else:
            return Response(data=self.serializer_class(message).data, status=201)


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):

        # Close old database connections to prevent usage of timed out connections
        close_old_connections()

        # Get the token
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(e)
            return None
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(decoded_data)
            # Will return a dictionary like -
            # {
            #     "token_type": "access",
            #     "exp": 1568770772,
            #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
            #     "user_id": 6
            # }

            # Get the user using ID
            user = get_user_model().objects.get(id=decoded_data["user_id"])

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))


class ChatCosumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(self.scope)

    async def receive_json(self, content, **kwargs):
        print(content)


emails = MessageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('emails', emails)
]

websocket_urlpatterns = [
    path('chat', ChatCosumer.as_asgi())
=======
from .models import Message, MessageSerializer
from django.db.models import Q
MESSAGE_FIELDS = {
    'sender': {'type': 'text', 'required': True},
    'receivers': {'type': 'text', 'required': True},
    'subject': {'type': 'text', 'required': True},
    'content': {'type': 'text', 'required': True},
    'date': {'type': 'date', 'required': True},
    'read': {'type': 'bool', 'required': False}
}


class MessageRepository(Repository):
    def __init__(self, model=Message):
        super().__init__(model)


class MessageServise(Service):
    def __init__(self, repository=MessageRepository()):
        super().__init__(repository, fields=MESSAGE_FIELDS)


class MessageViewSet(ViewSet):
    def __init__(self, serializer_class=MessageSerializer, service=MessageServise(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)

    def list(self, request, *args, **kwargs):
        email = request.GET.get('email')
        if email is None:
            return super().list(request=request)
        messeges = Message.objects.filter(Q(sender__contains=email) | Q(receivers__contains=email))
        if messeges:
            return Response(data=[self.serializer_class(i).data for i in messeges])
        return Response(data=[])


messages, message = MessageViewSet.get_urls()


urlpatterns = [
    path('', messages),
    path('<int:pk>', message)
>>>>>>> origin/main
]
