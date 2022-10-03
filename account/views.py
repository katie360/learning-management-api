from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, AccountManager
from .serializers import AccountSerializer, LoginSerializer
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import generics, permissions, serializers
from knox.models import AuthToken
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


class AccountViewSet(viewsets.ModelViewSet):
   queryset = Account.objects.all()
   serializer_class = AccountSerializer
   

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # return Response({
        #     "user": UserSerializer(user, context=self.get_serializer_context()).data,
        #     "token": AuthToken.objects.create(user)[1]
        # })
        return super(LoginAPI, self).post(request, format=None)


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_manager': user.is_manager,
            'is_teacher': user.is_teacher,
            'is_student': user.is_student,
        },
        'token': token
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_manager': user.is_manager,
                'is_teacher': user.is_teacher,
                'is_student': user.is_student,
            },
        })
    else:
        return Response('User is not authenticated', status=401)

class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": AccountSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
