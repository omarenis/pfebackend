from django.urls import path
from django.db.models import QuerySet
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet as RestViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, \
    HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework_simplejwt.tokens import RefreshToken
from common.views import ViewSet, extract_serialized_objects_response, return_serialized_data_or_error_response
from gestionusers.models import LocalisationSerializer, UserSerializer,PersonProfileSerializer,User
from gestionusers.services import LocalisationService, UserService, signup, login

localisation_service = LocalisationService()
user_service = UserService()

@api_view(['GET'])
def find(request):
    login_number = request.data.get('login_number')
    user = user_service.get_by({'login_number': login_number})
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'message': 'User not found'}, status=HTTP_404_NOT_FOUND)




@permission_classes([AllowAny])
@api_view(['POST'])
@csrf_exempt
def login_controller(request, *args, **kwargs):
    try:
        user = login(login_number=request.data.get('login_number'), password=request.data.get('password'))
        token = RefreshToken.for_user(user=user)
        serializer = PersonProfileSerializer(user.profile)
        return Response(data={
            "access": str(token.access_token),
            "refresh": str(token),
            "userId": user.id,
            "type_user": user.type_user,
            "name": user.name,
            "active":user.is_active,
            "profile":serializer.data
        })
    except Exception as exception:
        if isinstance(exception, PermissionError):
            status = HTTP_403_FORBIDDEN
        elif isinstance(exception, ValueError):
            status = HTTP_401_UNAUTHORIZED
        else:
            status = HTTP_404_NOT_FOUND
        return Response(data={'message': str(exception)}, status=status)


@permission_classes([AllowAny])
@api_view(['POST'])
@csrf_exempt
def signup_controller(request, *args, **kwargs):
    data = {}
    localisation = localisation_service.filter_by(request.data.get('localisation')).first()
    if localisation is None:
        localisation = localisation_service.create(data=request.data.get('localisation'))
    for i in user_service.fields:
        data[i] = request.data.get(i)
    data['localisation_id'] = localisation.id
    user = user_service.filter_by({'login_number': request.data.get('login_number')}).first()
    if user is not None:
        if user.is_active:
            return Response(data={'account with such login_number already created': True}, status=HTTP_401_UNAUTHORIZED)
           
        user_service.changestate(_id=user.id, data=request.data)
    else:
        user = signup(data)
    if isinstance(user, Exception):
        return Response(data={"error": str(user)}, status=500)
    else:
        return Response(data={
            "created successfully": True,
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
    def list(self, request):
        try:
            output = []

            if request.user.type_user == 'admin':
                users = self.service.list()
            elif request.user.type_user == 'school':
                users = self.service.filter_by({'profile__school__id': request.user.id})
            elif hasattr(request.user, 'profile') and request.user.profile.is_super_doctor:
                users = self.service.filter_by({'profile__super_doctor__id': request.user.profile_id})
            else:
                users = []

            for user in users:
                output.append(self.serializer_class(user).data)

            return Response(data=output, status=HTTP_200_OK)
        except Exception as exception:
            return Response(data={'error': str(exception)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

users_list, user_retrieve_update_delete = UserViewSet.get_urls()
urlpatterns = [
    path('', users_list),
    path('/<int:pk>', user_retrieve_update_delete),
    path('/login', login_controller),
    path('/signup', signup_controller),
    path('/logout', logout),
    path('/find',find)
]
