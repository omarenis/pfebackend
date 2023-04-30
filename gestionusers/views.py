from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet as RestViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, \
    HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework_simplejwt.tokens import RefreshToken
from common.views import ViewSet, extract_serialized_objects_response, return_serialized_data_or_error_response
from gestionusers.models import LocalisationSerializer, UserSerializer
from gestionusers.services import LocalisationService, LoginSignUpService, UserService


class TokenViewSet(RestViewSet):
    localisation_service = LocalisationService()
    login_sign_up_service = LoginSignUpService()
    service = UserService()

    def get_permissions(self):
        permissions = []
        if self.action == 'logout':
            permissions.append(IsAuthenticated())
        else:
            permissions.append(AllowAny())
        return permissions

    def login(self, request, *args, **kwargs):
        try:

            user = self.login_sign_up_service.login(login_number=request.data.get('login_number'),
                                                    password=request.data.get('password'))
            if isinstance(user, Exception):
                return Response(data={"error": str(user)}, status=500)
            token = RefreshToken.for_user(user=user)
            return Response(data={
                "access": str(token.access_token),
                "refresh": str(token),
                "userId": user.id,
                "typeUser": user.typeUser,
                "name": user.name,
                "familyName": user.familyName if hasattr(user, "familyName") else None,
                "is_super": user.is_super if hasattr(user, "is_super") else None
            })
        except Exception as exception:
            if isinstance(exception, PermissionError):
                status = HTTP_403_FORBIDDEN
            elif isinstance(exception, ValueError):
                status = HTTP_401_UNAUTHORIZED
            else:
                status = HTTP_404_NOT_FOUND
            return Response(data={'message': str(exception)}, status=status)

    def signup(self, request, *args, **kwargs):
        data = {}
        localisation = self.localisation_service.filter_by(request.data.get('localisation')).first()
        if localisation is None:
            localisation = self.localisation_service.create(data=request.data.get('localisation'))
        for i in self.service.fields:
            data[i] = request.data.get(i)
        data['localisation_id'] = localisation.id
        user = self.service.filter_by({'login_number': request.data.get('login_number')}).first()
        data['is_active'] = True
        if user is not None:
            if user.is_active:
                return Response(data={'created': True}, status=HTTP_401_UNAUTHORIZED)
            self.service.put(_id=user.id, data=data)
        else:
            user = self.login_sign_up_service.signup(data)
        if isinstance(user, Exception):
            return Response(data={"error": str(user)}, status=500)
        else:
            return Response(data={
                "created": True,
            }, status=HTTP_201_CREATED)


class LocalisationViewSet(ViewSet):

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes.append(AllowAny)
        else:
            permission_classes.append(IsAdminUser)
        return (permission() for permission in permission_classes)

    def __init__(self, fields=None, serializer_class=LocalisationSerializer, service=LocalisationService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


@csrf_exempt
@api_view(http_method_names=['POST'])
def logout(request, *args, **kwargs):
    token = RefreshToken(request.data.get('refresh'))
    token.blacklist()
    return Response(status=HTTP_204_NO_CONTENT)


class UserViewSet(ViewSet):
    def get_permissions(self):
        return [IsAuthenticated()]

    def __init__(self, serializer_class=UserSerializer, service=UserService(), **kwargs):
        super().__init__(serializer_class=serializer_class, service=service, **kwargs)
        self.localisation_service = LocalisationService()
        self.permission_classes = self.get_permissions()


users_list, user_retrieve_update_delete = UserViewSet.get_urls()
login = TokenViewSet.as_view({
    'post': 'login'
})
signup = TokenViewSet.as_view({
    'post': 'signup'
})
urlpatterns = [
    path('', users_list),
    path('/<int:pk>', user_retrieve_update_delete),
    path('/login', login),
    path('/signup', signup),
    path('/logout', logout),
]
