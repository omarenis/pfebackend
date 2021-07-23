from django.urls import path
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from common.views import ViewSet
from gestionusers.models import LocalisationSerializer, PersonSerializer
from gestionusers.services import LocalisationService, PersonService


class LocalisationViewSet(ViewSet):

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes.append(AllowAny)
        else:
            permission_classes.append(IsAdminUser)
        return [permission() for permission in permission_classes]

    def __init__(self, fields=None,
                 serializer_class=LocalisationSerializer,
                 service=LocalisationService(),
                 **kwargs):
        if fields is None:
            fields = {
                'governorate': {'type': 'text', 'required': True},
                'delegation': {'type': 'text', 'required': True},
                'zip_code': {'type': 'text', 'required': True}
            }
        super().__init__(fields, serializer_class, service, **kwargs)


class PersonViewSet(ViewSet):
    def __init__(self, serializer_class=PersonSerializer, service=PersonService(), fields=None, **kwargs):
        if fields is None:
            fields = {
                'name': {'type': 'text', 'required': True},
                'family_name': {'type': 'text', 'required': True},
                'cin': {'type': 'text', 'required': True},
                'email': {'type': 'email', 'required': True},
                'telephone': {'type': 'email', 'required': True},
                'password': {'type': 'password', 'required': True},
                'accountId': {'type': 'password', 'required': False},
                'localisation_id': {'type': 'integer', 'required': False}
            }
        super().__init__(fields=fields, serializer_class=serializer_class, service=service, **kwargs)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes.append(IsAdminUser)
        elif self.action == 'retrieve':
            permission_classes.append(IsAuthenticated)
        elif self.action == 'signup' or self.action == 'login':
            permission_classes.append(AllowAny)
        return [permission() for permission in permission_classes if permission is not None]

    def retrieve(self, request, pk=None, *args, **kwargs):
        user = self.service.retreive(pk)
        if user is None:
            return Response(data={"error": "لم يتم العثور على المستخدم"}, status=404)
        else:
            return Response(data=self.serializer_class(data=user).data, status=200)

    def login(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email is None:
            return Response(data={"error": "الحساب غير موجود"}, status=400)
        password = request.data.get('password')
        if password is None:
            return Response(data={"error": "كلمة المرور غير موجودة"}, status=400)
        user = self.service.login(email, password)
        if isinstance(user, Exception):
            return Response(data={"error": str(user)}, status=500)
        token = RefreshToken.for_user(user=user)
        return Response(data={
            "access": str(token.access_token),
            "refresh": str(token),
            "userId": user.id
        })

    def signup(self, request, *args, **kwargs):
        user = self.service.create(request.data)
        if isinstance(user, Exception):
            return Response(data={"error": str(user)}, status=500)
        else:
            token = RefreshToken.for_user(user=user)
            return Response(data={
                "access": str(token.access_token),
                "refresh": str(token),
                "userId": user.id
            })


users_list = PersonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_retrieve_update_delete = PersonViewSet.as_view({
    'delete': 'delete'
})
login = PersonViewSet.as_view({
    'post': 'login'
})
signup = PersonViewSet.as_view({
    'post': 'signup'
})
urlpatterns = [
    path('', users_list),
    path('<int:user_id>', user_retrieve_update_delete),
    path('login', login),
    path('signup', signup),
]
