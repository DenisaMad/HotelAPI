from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from ..models import User
from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ..models import Profile
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
#EXAMPLE OF CRUD OPERATIONS FOR CREATING A User:
from ..requests import CreateUserRequest, UpdateUserRequest
from ..serializers import UserSerializer, UserSerializerUpdate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 

class UserViewWithoutPk(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self,request):
        try:
            data = request.data 
            password = data['password']
            password2 = data['password2']
            if password != password2:
                return Response("Passwords must match",status=status.HTTP_400_BAD_REQUEST)
            response = UserSerializer(data=data)
            if response.is_valid():
                user = response.save()
                Profile.objects.create(email=data['email'],role=data['role'],user=user)
                return Response("Success",status=status.HTTP_201_CREATED)
            else:
                errors = response.errors
                return Response(errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("exceptie", e)
            return Response("Internal server error,please try again later",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(request_body=UpdateUserRequest)
    def put(self,request):
        data=request.data
        response=UpdateUserRequest(data=data)
        if not response.is_valid():
            return Response(response.errors,status=status.HTTP_400_BAD_REQUEST)
        user_id=data["user_id"]
        user=User.objects.get(id=user_id)
        profile= Profile.objects.get(user_id=user_id)
        response=UserSerializerUpdate(instance=user, data=data)
        if not response.is_valid():
             return Response(response.errors,status=status.HTTP_400_BAD_REQUEST)
        response.save()
        role=data["role"]
        profile.role=role
        profile.email=data["email"]
        profile.save()
        return Response("Success", status=status.HTTP_200_OK)
    def get(self,request):
        try:
            users = User.objects.all()
            usersConverted = UserSerializer(users,many=True)
            response = usersConverted.data
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response("Internal server error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserViewWithPk(APIView):

    def get(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            userConverted = UserSerializer(user,many=False)
            response = userConverted.data
            return Response(response,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("Your account could not be found",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("Internal server error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"]= user.email
        profile=Profile.objects.get(user=user)
        token["role"]= profile.role
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
